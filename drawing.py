#How to draw shapes

#required 
import pygame
pygame.init();

#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Drawing Shapes!")

pygame.display.update()		#only updates portion specified




gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	gameDisplay.fill(white)
	#look up draw.rect()
	pygame.draw.rect(gameDisplay, red, [50, 100, 10, 100])
	pygame.draw.rect(gameDisplay, red, [300, 100, 100, 20])

	gameDisplay.fill(blue, rect=[200,200, 20,20])
	pygame.draw.lines(gameDisplay, yellow, False, [(400,400), (450,350), (400,300), (400,400)], 5)
	gameDisplay.fill(green, rect=[200,300, 20,200])

	# gameDisplay.fill(blue, rect=[50,50, 20,20])
	pygame.draw.circle(gameDisplay, blue, (500,100), 20, 0)
	
	pygame.display.update()		




#required
pygame.quit()
quit()				#exits python