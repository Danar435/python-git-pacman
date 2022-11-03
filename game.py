# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg
from ghost import Ghost
from pacman import Pacman

# Screen setup
pg.init()
screen = pg.display.set_mode((600,800))
pg.display.set_caption("Pac-Man")
pg.display.set_icon(pg.image.load("images/pac1.png"))

pacman = Pacman(500,350)
ghost1 = Ghost(100,200, 0)
ghost2 = Ghost(100,300, 1)
ghost3 = Ghost(100,400, 2)
ghost4 = Ghost(100,500, 3)

direction = None
running = True
tick = 0

while running:

    # Event loop
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                direction = "left"
            if event.key == pg.K_RIGHT:
                direction = "right"
            if event.key == pg.K_UP:
                direction = "up"
            if event.key == pg.K_DOWN:
                direction = "down"
            if event.key == pg.K_ESCAPE:
                running = False

    # Logic
    pacman.move(direction)
    ghost1.logic(pacman.x, pacman.y)
    ghost2.logic(pacman.x, pacman.y)
    ghost3.logic(pacman.x, pacman.y)
    ghost4.logic(pacman.x, pacman.y)
    
    # Draw 
    screen.fill((255,255,255))
    pacman.draw(screen, direction, tick)
    ghost1.draw(screen)
    ghost2.draw(screen)
    ghost3.draw(screen)
    ghost4.draw(screen)

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    tick += 1
    time.sleep(0.05)