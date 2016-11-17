import pygame
pygame.init();

gameDisplay = pygame.display.set_mode((500,500))

##SAMPLE 4 CODE -- MODIFY!!!!
x_pos = 0
y_pos = 0

gameExit = False
while not gameExit:
	redraw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_pos -= 10
		if event.key == pygame.K_RIGHT:
			x_pos += 10
		if event.key == pygame.K_UP:
			y_pos -= 10
		if event.key == pygame.K_DOWN:
			y_pos += 10

##
pygame.quit()
quit()	