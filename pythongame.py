import pygame
from pygame import *
from pygame.sprite import *
import sys
import mixer
pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (230,0, 240)
yellow = (255, 255, 0)
gray = (70,70,70)

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((500,500))

class Player(pygame.sprite.Sprite): #user player
	def __init__(self, color):          
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([40, 40])
		self.image.fill(color)
		self.rect=self.image.get_rect().move(30, 30)
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
		self.rect = self.image.get_rect().move(50+self.x_delta, 50+self.y_delta)

class Barrier(pygame.sprite.Sprite): #barriers
	def __init__(self,width,height,a,b,color):          
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect=self.image.get_rect().move(a,b)

class Blocker(Barrier): #moving barriers
	def __init__(self,width,height,a,b,color,speed):          
		Barrier.__init__(self,width,height,a,b,color) 
		self.speed = speed
	def update(self):
		if 50 <= self.rect.y < 400:
			self.rect.y += self.speed
		elif self.rect.y >= 400:
			self.rect.y=50

class Flag(pygame.sprite.Sprite): #object to capture
	def __init__(self, color):          
		pygame.sprite.Sprite.__init__(self) 
		self.color=color
		self.image = pygame.Surface([24, 24])
		self.image.fill(black)
		self.rect=self.image.get_rect().move(450,450)
		pygame.draw.circle(self.image, self.color, (12,12), 12, 0)

def checkCollision(sprite1, sprite2): #checks for collision with barriers
	col = pygame.sprite.spritecollide(sprite1, sprite2, True)
	if col!=[]:
		font = pygame.font.Font(None, 100)
		text=font.render("GAME OVER", 1, yellow)
		gameDisplay.blit(text, (40, 200))
		pygame.display.update()
		print ("You lost.")
		pygame.time.delay(4000)
		sys.exit()

def draw(): #draws game display
	gameDisplay.fill(black)
	all_list.draw(gameDisplay)

#creation of game objects
wall1=Barrier(500, 10, 0, 0, red)
wall2=Barrier(500, 10, 0, 490, red)
wall3=Barrier(10, 500, 0, 0, red)
wall4=Barrier(10, 500, 490, 0, red)
c1=Barrier(40, 160, 200, 30, gray)
c2=Barrier(40, 160, 200, 270, gray)
block1=Blocker(50, 50, 75, 75, green, 4)
block2=Blocker(50, 50, 350, 75, purple, 4)
p=Player(blue)
f=Flag(white)

bar_list=Group(wall1,wall2,wall3,wall4, c1, c2) #list of barriers
block_list=Group(block1, block2) #list of blockers that move, need to update
bad_list=Group(bar_list, block_list) #list of objects that will cause harm
sprite_list=Group(p, f) #list of neutral objects
all_list=Group(bar_list, block_list, sprite_list) #list of all objects

start_ticks=pygame.time.get_ticks() #timer starter

def main(): ##MAIN GAME LOOP

	print ("You have 15 seconds to capture the white flag.")
	
	try: #music
		pygame.mixer.music.load("mozart.mp3")
		pygame.mixer.music.play(loops=-1)
	except:
		pass

	gameExit = False
	while not gameExit:
		draw()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

		if event.type == pygame.KEYDOWN: #moves player
			if event.key == pygame.K_LEFT:
				p.left()					
			if event.key == pygame.K_RIGHT:
				p.right()
			if event.key == pygame.K_UP:
				p.up()
			if event.key == pygame.K_DOWN:
				p.down()
			p.update()

		seconds=(pygame.time.get_ticks()-start_ticks)/1000 #timer
		if seconds>15:
			font=pygame.font.Font(None, 100)
			text=font.render("TIME'S UP", 1, yellow)
			gameDisplay.blit(text, (100, 200))
			pygame.display.update()
			print ("You ran out of time.")
			pygame.time.delay(4000)
			sys.exit()

		if p.rect.colliderect(f.rect): #checks if you captured flag
			all_list.remove(f)
			draw()
			font = pygame.font.Font(None, 50)
			text=font.render("You captured the flag!", 1, yellow)
			gameDisplay.blit(text, (80, 200))
			pygame.display.update()
			print ("You captured the flag in", seconds, "seconds!")
			pygame.time.delay(4000)
			sys.exit()
		
		checkCollision(p, bad_list) #checks if you hit a barrier, lost
		block_list.update()
		pygame.display.update()
		clock.tick(60)	

main()

pygame.quit()
quit()	