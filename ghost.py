import pygame as pg

class Ghost:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

    def logic(self, pacx, pacy):
        if self.x > pacx:
            self.x -= 4
        elif self.x < pacx:
            self.x += 4
        elif self.y > pacy:
            self.y -= 4
        elif self.y < pacy:
            self.y += 4

    def draw(self, screen):
        img = pg.image.load(f"images/ghost{self.num}.png")
        img = pg.transform.scale(img, (32,32))
        screen.blit(img, (self.x, self.y))  