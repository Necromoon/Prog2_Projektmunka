import pygame as pg

# Colors
BLACK = (0, 0, 0)
LIGHTGREY = (100, 100, 100)
LG = LIGHTGREY


# SCREEN
WIDTH = 1024
W = WIDTH
HEIGHT = 768
H = HEIGHT


# FPS
FPS = 120


# Title and Background
TITLE = "Projekt_Game"
BGCOLOR = BLACK


TILESIZE = 64
TS = TILESIZE
GRIDWIDTH = W / TS
GRIDHEIGHT = H / TS


# Wall
WALL_IMG = 'Wall.png'


# Player
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'Player.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)


# Enemy
ENEMY_IMG = 'Enemy.png'
ENEMY_SPEED = 150
ENEMY_HIT_RECT = pg.Rect(0, 0, 30, 30)
