import pygame, sys
from pygame.locals import *




class Tree(pygame.sprite.Sprite):
    def __init__(self, pos):
        # Call parent sprite class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.Surface([80,80])
        self.image =  pygame.image.load("tree.png").convert_alpha()
        self.image =  pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Projectile(pygame.sprite.Sprite):
    def __init__(self, centerx, centery):
        # Call parent sprite class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([1,1])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = centerx
        self.rect.y = centery

    def move(self):
    # Move bullets, could make different speeds based on types of projs
        self.rect.y -= 10
        # If bullet is off screen, die
        if self.rect.y <= 0:
            self.remove()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # Call parent sprite class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.Surface([60,60])
        self.image =  pygame.image.load("player.png").convert_alpha()
        self.image =  pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.y = 300

    def checkCollisions(self, bullets):
    	pygame.sprite.spritecollide(bullets, self, 0)


world1 = {
	'map':[Tree([300,100]), Tree([200,100]), Tree([50,400])],
	'ent':[Enemy()],
	'background':""

}


class Level:
	def __init__(self, world):
		self.entities = world['ent']

		self.world_sprites = pygame.sprite.Group()
		for obj in world['map']:
			self.world_sprites.add(obj)

	def run(self, bullets):
		for ent in self.entities:
			ent.checkCollisions(bullets)

	def render(self, surface):
		self.world_sprites.draw(surface)

	def scroll(self, amount):
		for spr in self.world_sprites:
			spr.rect.y += amount



class Hero(pygame.sprite.Sprite):
    def __init__(self):
        # Call parent sprite class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.Surface([60,60])
        self.image =  pygame.image.load("player.png").convert_alpha()
        self.image =  pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.y = 300

        self.hero_sprites = pygame.sprite.Group()
        self.hero_sprites.add(self)
        self.hero_bullet_sprites = pygame.sprite.Group()

    def moveBullets(self):
    	for b in self.hero_bullet_sprites:
        	b.move()


    def checkCollisions(self, mapObjs):
    	return pygame.sprite.spritecollide(self, mapObjs, 0)

    def shoot(self):
        # Get center of origin, for starting position of projectile
        centerx = self.rect.centerx
        centery = self.rect.centery

        snowball = Projectile(centerx, centery)
        self.hero_bullet_sprites.add(snowball)


    def move(self, mapObjs):
    	pressed = pygame.key.get_pressed()

    	moveSpeed = 2

    	xMove = 0
    	if pressed[pygame.K_LEFT]:
        	xMove -= moveSpeed
        if pressed[pygame.K_RIGHT]:
        	xMove += moveSpeed
        self.rect.x += xMove

        if self.checkCollisions(mapObjs):
        	self.rect.x -= xMove

        yMove = 0
    	if pressed[pygame.K_UP]:
        	yMove -= moveSpeed
        if pressed[pygame.K_DOWN]:
        	yMove += moveSpeed
        self.rect.y += yMove
        
        if self.checkCollisions(mapObjs):
        	self.rect.y -= yMove - moveSpeed - 2 ########## fix this bs

        if pressed[pygame.K_SPACE]:
        	self.shoot()



    def draw(self, surface):
    	self.moveBullets()
    	self.hero_sprites.draw(surface)
    	self.hero_bullet_sprites.draw(surface)







class Game:
	def __init__(self, surface):
		self.surface = surface
		self.currentLevel = Level(world1)
		self.hero = Hero()
		self.scrollFactor = 0
		self.totalScroll = 0

	def scroll(self):
		scrollAmount = 1

		self.currentLevel.scroll(scrollAmount)

		self.totalScroll += scrollAmount

	def render(self):

		self.surface.fill((255, 255, 255))
		self.hero.draw(self.surface)
		self.currentLevel.render(self.surface)
		pygame.display.update()



	def run(self):

		self.scroll()
		self.currentLevel.run(self.hero.hero_bullet_sprites)
		self.hero.move(self.currentLevel.world_sprites)
		self.render()
