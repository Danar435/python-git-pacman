import pygame as pg

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

        from game import tick

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
