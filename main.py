import sys
from os import path
from sprites import *
from tilemap import *


def draw_player_health(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)


# Game
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((W, H))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'map.txt'))
        self.player_img = pg.image.load(path.join(game_folder, PLAYER_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(game_folder, BULLET_IMG)).convert_alpha()
        self.enemy_img = pg.image.load(path.join(game_folder, ENEMY_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(game_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TS, TS))

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '*':
                    Wall(self, col, row)
                if tile == 'E':
                    Enemy(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
        hits = pg.sprite.spritecollide(self.player, self.enemies, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= ENEMY_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.pos += vec(ENEMY_KNOCKBACK, 0).rotate(-hits[0].rot)
        hits = pg.sprite.groupcollide(self.enemies, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0, 0)

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)
        for sprite in self.all_sprites:
            if isinstance(sprite, Enemy):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
