import pygame
import math
import random

pygame.init()

clock = pygame.time.Clock()

size = (1920, 1080)
screen = pygame.display.set_mode(size)

MOVE = 2.5

WHITE = (255, 255, 255)
RED = (255, 0, 0)


class player(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y, a, b):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.x = a
        self.y = b

    def moveRight_P(self, pixels):
        self.rect.x += pixels
        pass

    def moveLeft_P(self, pixels):
        self.rect.x -= pixels
        pass

    def moveUp_P(self, pixels):
        self.rect.y -= pixels
        pass

    def moveDown_P(self, pixels):
        self.rect.y += pixels
        pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, pos, radius, width):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.circle(self.image, color, [radius, radius], radius, width)
        self.rect = self.image.get_rect()
        self.speed = 1
        self.pos = pygame.Vector2(pos[0], pos[1])

    def draw(self):
        self.rect.center = (int(round(self.pos.x)), int(round(self.pos.y)))
        screen.blit(self.image, self.rect)

    def move_towards_Player(self, Player):
        deltaVec = pygame.Vector2(Player.rect.center) - self.pos
        len = deltaVec.length()
        if len > 0:
            self.pos += deltaVec / len * min(len, self.speed)

    def moveRight_E(self, pixels):
        self.rect.x += pixels
        pass

    def moveLeft_E(self, pixels):
        self.rect.x -= pixels
        pass

    def moveUp_E(self, pixels):
        self.rect.y -= pixels
        pass

    def moveDown_E(self, pixels):
        self.rect.y += pixels
        pass


class bullet(pygame.sprite.Sprite):
    def __init__(self, a, b, mouse_x, mouse_y):
        super().__init__()
        self.x = a
        self.y = b
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.lifetime = 300
        self.speed = 8
        self.angle = math.atan2(mouse_y - b, mouse_x - a)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.radius = 5

    def draw(self):
        self.x += int(self.x_vel)
        self.y += int(self.y_vel)

        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)
        self.lifetime -= 1


player = player("player.png", 0, 0, 0, 0)
player_group = pygame.sprite.Group()
player_group.add(player)

enemy_list = []
enemy_rad = 15
enemy_dist = (200, 900)
next_enemy_time = pygame.time.get_ticks() + 10000

bullets = []

run = True
while run:

    screen.fill((50, 0, 255))
    clock.tick(120)
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullets.append(bullet(player.x, player.y, x, y))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.moveLeft_P(MOVE)
    if keys[pygame.K_d]:
        player.moveRight_P(MOVE)
    if keys[pygame.K_w]:
        player.moveUp_P(MOVE)
    if keys[pygame.K_s]:
        player.moveDown_P(MOVE)

    current_time = pygame.time.get_ticks()
    if current_time > next_enemy_time:
        next_enemy_time = current_time + 2000

        on_screen_rect = pygame.Rect(enemy_rad, enemy_rad, size[0] - 2 * enemy_rad, size[1] - 2 * enemy_rad)
        enemy_pos = (-1, -1)
        while not on_screen_rect.collidepoint(enemy_pos):
            dist = random.randint(*enemy_dist)
            angle = random.random() * math.pi * 2
            p_pos = (player.rect.centerx, player.rect.centery)
            enemy_pos = (p_pos[0] + dist * math.sin(angle), p_pos[1] + dist * math.cos(angle))

        new_pos = (random.randrange(0, size[0]), random.randrange(0, size[1]))
        new_enemy = Enemy(RED, enemy_pos, enemy_rad, 0)
        enemy_list.append(new_enemy)

    for enemy in enemy_list:
        enemy.move_towards_Player(player)

    for enemy in enemy_list:
        enemy.draw()

    for bullet_ in bullets:
        if bullet_.lifetime <= 0:
            bullets.pop(bullets.index(bullet_))
        bullet_.draw()

    player_group.draw(screen)
    pygame.display.update()
