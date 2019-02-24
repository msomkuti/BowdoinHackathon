import pygame, sys
from pygame.locals import *




class Tree:
	def __init__(self, pos):
		self.rect = pygame.Rect(pos[0], pos[1], 100, 100)
		self.image = pygame.image.load("tree.png")

	def draw(self, surface):
		surface.blit(self.image, self.rect)





world1 = {
	'map':[Tree([30,100])],
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



class Game:
	def __init__(self, surface):
		self.surface = surface
		self.currentLevel = Level(world1)

	def render(self):
		self.currentLevel.render(self.surface)


	def run(self):
		self.render()
