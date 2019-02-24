import pygame, sys
from pygame.locals import *
from random import randint



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
        self.image = pygame.Surface([7,7])
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

#### STOCK ENEMY
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        # Call parent sprite class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.Surface([60,60])
        self.image =  pygame.image.load("Snowman2.png").convert_alpha()
        self.image =  pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


        self.health = 10

    def checkCollisions(self, bullets):
    	if pygame.sprite.spritecollide(self, bullets, 1):
    		self.health -= 1
    	if self.health <= 0:
    		self.kill()

    def move(self):
    	return 0
############## 



class SideEnemy(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        # Call parent sprite class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.Surface([60,60])
        self.image =  pygame.image.load("Snowman2.png").convert_alpha()
        self.image =  pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.direction = direction
        self.velocity = 40

    def checkCollisions(self, bullets):
    	return 0

    def move(self):
    	self.rect.x += self.direction * self.velocity


class TurretEnemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        # Call parent sprite class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.Surface([60,60])
        self.image =  pygame.image.load("Snowman2.png").convert_alpha()
        self.image =  pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


        self.health = 5

    def checkCollisions(self, bullets):
    	if pygame.sprite.spritecollide(self, bullets, 1):
    		self.health -= 1
    	if self.health <= 0:
    		self.kill()

    def move(self):
    	return 0     		

 

world1 = {
	'map':[Tree([300,-100]), Tree([200,-180]), Tree([50,-100])],
	'ent':[Enemy([100, 100]), SideEnemy([-100, 0], 1)],
	'background':""

}


class Level:
	def __init__(self, world):

		self.world_sprites = pygame.sprite.Group()
		self.entity_sprites = pygame.sprite.Group()
		for obj in world['map']:
			self.world_sprites.add(obj)

		for ent in world['ent']:
			self.entity_sprites.add(ent)

	def run(self, bullets):
		for ent in self.entity_sprites:
			ent.checkCollisions(bullets)
			ent.move()

	def render(self, surface):
		self.world_sprites.draw(surface)
		self.entity_sprites.draw(surface)

	def scroll(self, amount):
		for spr in self.world_sprites:
			spr.rect.y += amount



class Hero(pygame.sprite.Sprite):
    def __init__(self):
        # Call parent sprite class constructor
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.Surface([60,60])
        self.image =  pygame.image.load("Skier.png").convert_alpha()
        self.image =  pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.y = 300

        self.hero_sprites = pygame.sprite.Group()
        self.hero_sprites.add(self)
        self.hero_bullet_sprites = pygame.sprite.Group()
        self.cooldown = 0

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
        	new_time = pygame.time.get_ticks()
        	if (new_time - self.cooldown) > 200:
        		self.shoot()
        		self.cooldown = new_time
        	print(new_time)



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
