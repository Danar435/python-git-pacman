# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("hello, innit", x, y)

    def move(self, new_direction):
        if new_direction == "left":
            self.x -= 4
        elif new_direction == "right":
            self.x += 4
        elif new_direction == "up":
            self.y -= 4
        elif new_direction == "down":
            self.y += 4

    def draw(self, screen, new_direction):

        pacman_images = []
        for i in range(2):
            img = pg.image.load(f"images/pac{i}.png")
            img = pg.transform.scale(img, (32,32))
            pacman_images.append(img)

        r = int((tick/3)%2)
        if new_direction == "right":
            screen.blit(pacman_images[r], (self.x, self.y))
        elif new_direction == "left":
            screen.blit(pg.transform.rotate(pacman_images[r],180), (self.x, self.y))
        elif new_direction == "down":
            screen.blit(pg.transform.rotate(pacman_images[r],-90), (self.x, self.y))
        elif new_direction == "up":
            screen.blit(pg.transform.rotate(pacman_images[r],90), (self.x, self.y))
        else:
            screen.blit(pacman_images[0], (self.x, self.y))  

class Ghost:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        print("boo im a ghost", x, y)

    def draw(self, screen):
        img = pg.image.load(f"images/ghost{self.num}.png")
        img = pg.transform.scale(img, (32,32))
        screen.blit(img, (self.x, self.y))  

## Screen setup ##
pg.init()
screen = pg.display.set_mode((600,800))
pg.display.set_caption("Pac-Man")
pg.display.set_icon(pg.image.load("images/pac0.png"))

pacman = Pacman(100,100)
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
    
    # Draw 
    screen.fill((0,0,0))
    pacman.draw(screen, direction)
    ghost1.draw(screen)
    ghost2.draw(screen)
    ghost3.draw(screen)
    ghost4.draw(screen)

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    tick += 1
    time.sleep(0.05)