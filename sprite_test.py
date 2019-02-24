import pygame as pg

class hero(pg.sprite.Sprite):
    def __init__(self, image):
        # Call parent sprite class constructor
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([20,20])
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

    def move(self, pixels, move_key):
        self.rect.x += pixels

pg.init()

size = (600, 600)
screen = pg.display.set_mode(size)
hero1 = hero("player.png")
sprites = pg.sprite.Group() #hold and manage sprites
sprites.add(hero1)



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            False

    screen.fill((255,255,255))

    pressed = pg.key.get_pressed()  # Get state of all buttons

    if pressed[pg.K_UP]:
        hero.move(hero1, 1, "up")
    if pressed[pg.K_DOWN]:
        hero.move(hero1,5, "down")
    if pressed[pg.K_LEFT]:
        hero.move(hero1,5, "left")
    if pressed[pg.K_RIGHT]:
        hero.move(hero1,5, "right")

    sprites.draw(screen)

    pg.display.update()