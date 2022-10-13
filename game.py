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

direction = None
running = True
tick = 0
while running:

    # Event loop

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                direction = "left"
            elif event.key == pg.K_RIGHT:
                direction = "right"
            elif event.key == pg.K_UP:
                direction = "up"
            elif event.key == pg.K_DOWN:
                direction = "down"
            elif event.key == pg.K_ESCAPE:
                running = False

    # Move

    if direction == "left":
        x = x - 4
    elif direction == "right":
        x = x + 4
    elif direction == "up":
        y = y - 4
    elif direction == "down":
        y = y + 4

    # Draw level #

    screen.fill((255,255,255))
    for r, row in enumerate(level):
        for c, tile in enumerate(row):
            left = c*32
            top = r*32
            if tile == "#":
                pg.draw.rect(screen, (20,20,220), pg.Rect(left+1, top+1, 30,30), 1)
                #print(left, top, x, y)

                # collision

                if x+32 > left and x < left+32 :
                    if y+32 > top and y < top+32:
                        if direction == "right":
                            x = x - 4
                        if direction == "left":
                            x = x + 4
                        if direction == "down":
                            y = y - 4
                        if direction == "up":
                            y = y + 4
                        direction = None

    # Draw pacman#

    r = int((tick/3)%2)
    if direction == "right":
        screen.blit(pacman_images[r], (x, y))
    elif direction == "left":
        screen.blit(pg.transform.rotate(pacman_images[r],180), (x, y))
    elif direction == "down":
        screen.blit(pg.transform.rotate(pacman_images[r],-90), (x, y))
    elif direction == "up":
        screen.blit(pg.transform.rotate(pacman_images[r],90), (x, y))
    else:
        screen.blit(pacman_images[0], (x, y))  

    # Update screen

    pg.display.flip()

    # Framerate (limit by doing nothing)

    tick += 1
    time.sleep(0.05)
