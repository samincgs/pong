import pygame
from os.path import join
from pygame import Vector2 as vector

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
SIZE = {'paddle': (40, 100), 'ball' : (30, 30)}
POS = {'player' : (WINDOW_WIDTH - 40, WINDOW_HEIGHT / 2), 'opponent' : (40, WINDOW_HEIGHT / 2)}
SPEED = {'player': 500, 'opponent:': 250, 'ball': 450}
COLORS = {
   'bg': '#002633',
    'paddle' : '#ee322c',
    'paddle shadow' : '#b12521',
    'ball' : '#ee622c',
    'ball shadow' : '#c14f24'
}