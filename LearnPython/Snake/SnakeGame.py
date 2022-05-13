# Simple Snake game in Python 3 
# By @Nihar 

import math
import random
from turtle import width
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface, eyes=False):
        pass


def drawGrid(w, rows, surface):
    sizeBetween = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x += sizeBetween
        y += sizeBetween
        pygame.draw.line(surface, (192, 192, 192), (x,0), (x, w))
        pygame.draw.line(surface, (192, 192, 192), (0,y), (w, y))


def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10,10))
    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)

main()

pygame.display.quit()
pygame.quit()