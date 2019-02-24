import pygame as pg

class projectile(pg.sprite.Sprite):
    def __init__(self, centerx, centery):
        # Call parent sprite class constructor
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([1,1])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = centerx
        self.rect.y = centery

    def move(self):
    # Move bullets, could make different speeds based on types of projs
        self.rect.y -= 10

        # If bullet is off screen, die
        if b.rect.y <= 0:
            b.remove()