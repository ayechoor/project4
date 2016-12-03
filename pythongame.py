import pygame
from pygame import *
from pygame.sprite import *
import random
import sys
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (230,0, 240)
yellow = (255, 255, 0)
gray = (70,70,70)

speed = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((500,500))

class Player(pygame.sprite.Sprite): 
	def __init__(self, color):          
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([24, 24])
		self.image.fill(color)
		self.rect=self.image.get_rect()
		self.x_delta=0	
		self.y_delta=0
	def down(self):
		self.y_delta += 10
	def up(self):
		self.y_delta -= 10
	def left(self):
		self.x_delta -= 10
	def right(self):
		self.x_delta += 10
	def update(self):
		self.rect = self.image.get_rect().move(self.x_delta, self.y_delta)

class Barrier(pygame.sprite.Sprite):
	def __init__(self,width,height,a,b):          
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([width, height])
		self.image.fill(red)
		self.rect=self.image.get_rect().move(a,b)

class Flag(pygame.sprite.Sprite):
	def __init__(self, color):          
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([24, 24])
		self.image.fill(black)
		self.rect=self.image.get_rect()
		pygame.draw.circle(self.image, color, (12,12), 12, 0)

def checkCollision(sprite1, sprite2):
	col = pygame.sprite.spritecollide(sprite1, sprite2, True)
	if col!=[]:
		font = pygame.font.Font(None, 100)
		text=font.render("GAME OVER", 1, yellow)
		gameDisplay.blit(text, (40, 200))
		pygame.display.update()
		print ("You lost.")
		pygame.time.delay(4000)
		sys.exit()


b1=Barrier(300, 50, 0, 60)
b2=Barrier(50, 400, 100, 300)
b3=Barrier(50, 400, 300, 300)
b4=Barrier(300, 50, 200, 175)
p=Player(white)
f=Flag(blue)

bar_list=Group(b1, b2, b3, b4)
sprite_list=Group(p, f)
all_list=Group(bar_list, sprite_list)

def main():

	gameExit = False
	while not gameExit:
		gameDisplay.fill(black)
		all_list.draw(gameDisplay)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

		if p.rect.colliderect(f.rect):
			sprite_list.remove(f)
			#f.update()
			#sprite_list.add(f)
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				p.left()					
			if event.key == pygame.K_RIGHT:
				p.right()
			if event.key == pygame.K_UP:
				p.up()
			if event.key == pygame.K_DOWN:
				p.down()
			p.update()

		sprite_list.update()
		checkCollision(p, bar_list)

		pygame.display.update()
		speed.tick(27)	
				

main()

pygame.quit()
quit()	