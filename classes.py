import pygame, sys
from pygame.locals import *
import random



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

class enemyProjectile(pygame.sprite.Sprite):
   def __init__(self, centerx, centery, targetx, targety):
       # Call parent sprite class constructor
       pygame.sprite.Sprite.__init__(self)
       self.image =  pygame.Surface([10,10])
       self.image =  pygame.image.load("Snowbomb.png").convert_alpha()
       self.image =  pygame.transform.scale(self.image, (10, 10))
       self.rect = self.image.get_rect()

       self.b = centery
       self.rect.x = centerx
       self.rect.y = centery
       self.destinationx = targetx
       self.destinationy = targety

       self.velocX = 1.3 *  (targetx - self.rect.x) / (targety - self.rect.y)
       self.velocY = 1.3 * (targety - self.rect.y) / (targetx - self.rect.x)

       #self.slope = (targety - self.rect.y) / (targetx - self.rect.x)


       print(self.destinationy)
       print(self.destinationx)


   def move(self):
   # Move bullets, could make different speeds based on types of projs
       self.rect.x += self.velocX
       self.rect.y += self.velocY
       # If bullet is off screen, die
       if self.rect.y > 2000:
           self.remove()

   def check(self, enemies):
       return  pygame.sprite.spritecollide(self, enemies, 0)


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

    def move(self, target, bullets):
    	self.rect.x += self.direction * self.velocity




class Turret(pygame.sprite.Sprite):
    def __init__(self, pos):
       # Call parent sprite class constructor
       pygame.sprite.Sprite.__init__(self)
       self.image =  pygame.Surface([70, 70])
       self.image =  pygame.image.load("Snowman2.png").convert_alpha()
       self.image =  pygame.transform.scale(self.image, (70, 70))
       self.rect = self.image.get_rect()
       self.health = 10
       self.cooldown = 0
       self.rect.x = pos[0]
       self.rect.y = pos[1]

    def shoot(self, target, bullets):
       # Get center of origin, for starting position of projectile
       centerx = self.rect.centerx
       centery = self.rect.centery

       target_locx = target.rect.x
       target_locy = target.rect.y

       coal = enemyProjectile(centerx, centery, target_locx, target_locy)
       bullets.add(coal)



    def checkCollisions(self, bullets):
    	if pygame.sprite.spritecollide(self, bullets, 1):
    		self.health -= 1
    	if self.health <= 0:
    		self.kill()

    def move(self, target, bullets):
    	new_time = pygame.time.get_ticks()
        if (new_time - self.cooldown) > 800:
        	self.shoot(target, bullets)
        	self.cooldown = new_time

 

world1 = {
	'map':[],
	'ent':[],
	'background':""

}


class Level:
	def __init__(self, world):

		self.world_sprites = pygame.sprite.Group()
		self.entity_sprites = pygame.sprite.Group()
		self.bullet_sprites = pygame.sprite.Group()
		for obj in world['map']:
			self.world_sprites.add(obj)

		for ent in world['ent']:
			self.entity_sprites.add(ent)

	def run(self, bullets, target):
		for ent in self.entity_sprites:
			ent.checkCollisions(bullets)
			ent.move(target, self.bullet_sprites)
		for b in self.bullet_sprites:
			b.move()
			b.check(target.hero_sprites)

	def render(self, surface):
		self.world_sprites.draw(surface)
		self.entity_sprites.draw(surface)
		self.bullet_sprites.draw(surface)

	def scroll(self, amount):
		for spr in self.world_sprites:
			spr.rect.y += amount

		for ent in self.entity_sprites:
			ent.rect.y += amount

		rand = random.randint(1, 500)

		if rand < 5:
			nx = random.randint(1,1200)
			ny = -100
			self.world_sprites.add(Tree([nx, ny]))

		if rand > 497:
			nx = random.randint(1,1200)
			ny = -100
			self.entity_sprites.add(Turret([nx, ny]))



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
		self.currentLevel.run(self.hero.hero_bullet_sprites, self.hero)
		self.hero.move(self.currentLevel.world_sprites)
		self.render()
