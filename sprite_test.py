import pygame as pg
from projectile import *

class hero(pg.sprite.Sprite):
    def __init__(self, image):
        # Call parent sprite class constructor
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([20,20])
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
            self.rect.x += pixels
    def moveLeft(self, pixels):
            self.rect.x -= pixels
    def moveUp(self, pixels):
            self.rect.y -= pixels
    def moveDown(self, pixels):
            self.rect.y += pixels

    def shoot(self):
        # Get center of origin, for starting position of projectile
        centerx = self.rect.centerx
        centery = self.rect.centery

        snowball = projectile(centerx, centery)
        bullets.add(snowball)

pg.init()

size = (600, 600)
screen = pg.display.set_mode(size)
hero1 = hero("player.png")
sprites = pg.sprite.Group() # hold and manage sprites
bullets = pg.sprite.Group() # hold bullets
sprites.add(hero1)

go = 1
clock = pg.time.Clock()

while go == 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            go == 0

    screen.fill((255,255,255))

    # Key presses
    pressed = pg.key.get_pressed()  # Get state of all buttons
    if pressed[pg.K_UP]:
        hero1.moveUp(1)
    if pressed[pg.K_DOWN]:
        hero1.moveDown(1)
    if pressed[pg.K_LEFT]:
        hero1.moveLeft(1)
    if pressed[pg.K_RIGHT]:
        hero1.moveRight(1)
    if pressed[pg.K_SPACE]:
        hero1.shoot()

    # Draw sprites to screen
    sprites.draw(screen)

    for b in bullets:
        b.move()
    bullets.draw(screen)

    pg.display.update()
    clock.tick(60)

pg.quit()