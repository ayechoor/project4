import pygame
from pygame import *
from pygame.sprite import *
import random
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

speed = pygame.time.Clock()

class Player(pygame.sprite.Sprite): 
	def __init__(self):          
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([24, 24])
		self.image.fill(green)
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


def main():

	gameDisplay = pygame.display.set_mode((500,500))
	
	
	p1=Player()
	b1=Barrier(300, 50, 0, 50)
	b2=Barrier(50, 400, 100, 300)
	b3=Barrier(50, 400, 300, 300)
	b4=Barrier(300, 50, 200, 150)

	sprite_list=Group(p1, b1, b2, b3, b4)

	gameExit = False
	while not gameExit:
		gameDisplay.fill(black)
		sprite_list.draw(gameDisplay)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				p1.left()					
			if event.key == pygame.K_RIGHT:
				p1.right()
			if event.key == pygame.K_UP:
				p1.up()
			if event.key == pygame.K_DOWN:
				p1.down()
		
			p1.update()
		pygame.display.update()
		speed.tick(27)	
				

main()

pygame.quit()
quit()	