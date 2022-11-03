import pygame as pg

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == "left":
            self.x -= 4
        elif direction == "right":
            self.x += 4
        elif direction == "up":
            self.y -= 4
        elif direction == "down":
            self.y += 4

    def draw(self, screen, direction, tick):

        pacman_images = []
        for i in range(2):
            img = pg.image.load(f"images/pac{i}.png")
            img = pg.transform.scale(img, (32,32))
            pacman_images.append(img)

        r = int((tick/3)%2)
        if direction == "right":
            screen.blit(pacman_images[r], (self.x, self.y))
        elif direction == "left":
            screen.blit(pg.transform.rotate(pacman_images[r],180), (self.x, self.y))
        elif direction == "down":
            screen.blit(pg.transform.rotate(pacman_images[r],-90), (self.x, self.y))
        elif direction == "up":
            screen.blit(pg.transform.rotate(pacman_images[r],90), (self.x, self.y))
        else:
            screen.blit(pacman_images[0], (self.x, self.y))  
