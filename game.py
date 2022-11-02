# Pac-Man clone made for learning/teaching

import time
import random
import pygame as pg

## Sound Setup ##

pg.mixer.pre_init(44100,32,2,1024)
pg.mixer.init()
pg.mixer.music.load("pacman_banging.wav")
pg.mixer.music.play(loops = -1)

## Screen setup ##

pg.init()
screen = pg.display.set_mode((352,480))
pg.display.set_caption("Pac-Man (clone)")

## Load images ##

pacman_images = []
for i in range(2):
    img = pg.image.load(f"images/pac{i}.png")
    img = pg.transform.scale(img, (32,32))
    pacman_images.append(img)

## Level ##

level = []
with open('level.txt', 'r') as level_file:
    for r, line in enumerate(level_file):
        row = []
        for c, char in enumerate(line):
            if char == "#":
                row.append("#")
            elif char == "p":
                y = r*32
                x = c*32
                row.append(" ")
            else:
                row.append(" ")

        level.append(row)

num_rows = len(level)
num_cols = len(level[0])

## Game Loop ##

currentdir = None
nextdir = None

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
                if not currentdir:
                    currentdir = "left"
                elif currentdir == "right":
                    currentdir = "left"
                else:
                    nextdir = "left"
            elif event.key == pg.K_RIGHT:
                if not currentdir:
                    currentdir = "right"
                elif currentdir == "left":
                    currentdir = "right"
                else:
                    nextdir = "right"
            elif event.key == pg.K_UP:
                if not currentdir:
                    currentdir = "up"
                elif currentdir == "down":
                    currentdir = "up"
                else:
                    nextdir = "up"
            elif event.key == pg.K_DOWN:
                if not currentdir:
                    currentdir = "down"
                elif currentdir == "up":
                    currentdir = "down"
                else:
                    nextdir = "down"
            elif event.key == pg.K_ESCAPE:
                running = False

    # Move

    if currentdir == "left":
        x = x - 4
    elif currentdir == "right":
        x = x + 4
    elif currentdir == "up":
        y = y - 4
    elif currentdir == "down":
        y = y + 4

    # Draw level #

    screen.fill((255,255,255))
    for r, row in enumerate(level):
        for c, tile in enumerate(row):
            left = c*32
            top = r*32
            if tile == "#":
                pg.draw.rect(screen, (0,0,0), pg.Rect(left+2, top+2, 28,28), 2)
                #print(left, top, x, y)

                # Collision # 

                if x+32 > left and x < left+32 :
                    if y+32 > top and y < top+32:
                        if currentdir == "right":
                            x = x - 4
                        if currentdir == "left":
                            x = x + 4
                        if currentdir == "down":
                            y = y - 4
                        if currentdir == "up":
                            y = y + 4
                        currentdir = nextdir
                        nextdir = None

    # Draw pacman#

    r = int((tick/3)%2)
    if currentdir == "right":
        screen.blit(pacman_images[r], (x, y))
    elif currentdir == "left":
        screen.blit(pg.transform.rotate(pacman_images[r],180), (x, y))
    elif currentdir == "down":
        screen.blit(pg.transform.rotate(pacman_images[r],-90), (x, y))
    elif currentdir == "up":
        screen.blit(pg.transform.rotate(pacman_images[r],90), (x, y))
    else:
        screen.blit(pacman_images[0], (x, y))  

    # Update screen

    pg.display.flip()

    # Framerate (limit by doing nothing)

    tick += 1
    time.sleep(0.05)
