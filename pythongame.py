import pygame
from pygame import *
pygame.init()

gameDisplay = pygame.display.set_mode((500,500))

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Snake(pygame.sprite.Sprite): 

	def __init__(self):          
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.surface.Surface([20, 20])
		x_pos = 0
		y_pos = 0
		x_delta=0
		y_delta=0 
		self.rect = rect(x_pos,y_pos, 20, 20)
	def update(self):
		self.inflate_ip(10,10)
		if event.key == pygame.K_LEFT:
			x_delta -= 10
		if event.key == pygame.K_RIGHT:
			x_delta += 10
		if event.key == pygame.K_UP:
			y_delta -= 10
		if event.key == pygame.K_DOWN:
			y_delta += 10
		self.rect = rect(x_pos,y_pos)	

def main():

	speed = pygame.time.Clock()

	nag=Snake()

	gameExit = False
	while not gameExit:
		gameDisplay.fill(black)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				nag.update()
		pygame.display.update()	
		speed.tick(10)

main()

pygame.quit()
quit()	