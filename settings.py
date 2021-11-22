import pygame as pg

vec = pg.math.Vector2

# Colors
WHITE = (255, 255, 255)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)


# SCREEN
WIDTH = 1024
W = WIDTH
HEIGHT = 768
H = HEIGHT


# FPS
FPS = 120


# Title and Background
TITLE = "Projekt_Game"
BGCOLOR = BROWN


# Tile
TILESIZE = 64
TS = TILESIZE
GRIDWIDTH = W / TS
GRIDHEIGHT = W / TS


# Player
PLAYER_HEALTH = 100
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'Player.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)


# Enemy
ENEMY_IMG = 'Enemy.png'
ENEMY_SPEED = 150
ENEMY_HIT_RECT = pg.Rect(0, 0, 30, 30)
ENEMY_HEALTH = 100
ENEMY_DAMAGE = 10
ENEMY_KNOCKBACK = 20


# Bullet
BULLET_IMG = 'Bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10


# Wall
WALL_IMG = 'Wall.png'
