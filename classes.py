import pygame, sys
from pygame.locals import *




class Tree(pygame.sprite.Sprite):
    def __init__(self, pos):
        # Call parent sprite class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.Surface([20,20])
        self.image =  pygame.image.load("tree.png").convert_alpha()
        self.image =  pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()




world1 = {
	'map':[],
	'ent':[],
	'background':""

}


class Level:
	def __init__(self, world):
		self.level_map = world['map']
		self.entities = world['ent']

	def render(self, surface):
		for obj in self.level_map:
			obj.draw(surface)    

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        # Call parent sprite class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.Surface([20,20])
        self.image =  pygame.image.load("player.png").convert_alpha()
        self.image =  pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

    def move(self):
    	pressed = pygame.key.get_pressed()

    	if pressed[pygame.K_LEFT]:
        	self.rect.x -= 1
        if pressed[pygame.K_RIGHT]:
        	self.rect.x += 1
        if pressed[pygame.K_UP]:
        	self.rect.y -= 1
        if pressed[pygame.K_DOWN]:
        	self.rect.y += 1


class Game:
	def __init__(self, surface):
		self.surface = surface
		self.currentLevel = Level(world1)
		self.hero = Hero()
		self.hero_sprites = pygame.sprite.Group()
		self.hero_sprites.add(self.hero)

	def render(self):

		self.surface.fill((255, 255, 255))
		self.hero_sprites.draw(self.surface)
		#self.currentLevel.render(self.surface)
		pygame.display.update()


	def run(self):
		self.hero.move()
		self.render()
