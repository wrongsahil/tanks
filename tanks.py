import pygame
import time
import math

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 155, 0)
light_green = (0, 255, 0)

font_large = pygame.font.SysFont(None, 150)
font_medium = pygame.font.SysFont(None, 50)
font_small = pygame.font.SysFont(None, 40)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tanks")

clock = pygame.time.Clock()

def draw_tank(x, y, x_gun, y_gun):
	pygame.draw.circle(gameDisplay, black, (x, y), 10)
	pygame.draw.rect(gameDisplay, black, (x-20, y, 40, 20))

	for wheel_x in range(x-15, x+16, 5):
		pygame.draw.circle(gameDisplay, black, (wheel_x, y+22), 5)

	#x_gun = x
	#y_gun = y - int (math.sqrt(400-((x_gun-x)**2)))

	pygame.draw.line(gameDisplay, black, (x, y), (x_gun, y_gun), 5)

def gameloop():
	gameExit = False
	
	x = 400
	y = 553
	x_gun = x-20
	y_gun = y - int (math.sqrt(400-((x_gun-x)**2)))
	change_x_gun = 0
	change_x = 0

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gameExit = True
				elif event.key == pygame.K_d:
					change_x_gun =1
				elif event.key == pygame.K_a:
					change_x_gun = -1
				elif event.key == pygame.K_LEFT:
					change_x = -1
				elif event.key == pygame.K_RIGHT:
					change_x = 1

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					change_x_gun = 0
				elif event.key == pygame.K_d:
					change_x_gun = 0
				elif event.key == pygame.K_RIGHT:
					change_x = 0
				elif event.key == pygame.K_LEFT:
					change_x = 0

		if (x_gun+change_x_gun) >= (x-20) and (x_gun + change_x_gun) <= (x+20):
			x_gun += change_x_gun
			y_gun = y - int (math.sqrt(400-((x_gun-x)**2)))

		x += change_x
		x_gun +=change_x


		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, green, (0, 580, 800, 20))
		draw_tank(x, y, x_gun, y_gun)
		pygame.display.update()

		clock.tick(50)

	pygame.quit()
	quit()

def menu():

	gameIntro = True
	gameExit = False
	
	while gameIntro:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gameExit = True

		if gameExit == True:
			pygame.quit()
			quit()

		pos = pygame.mouse.get_pos()
		press = pygame.mouse.get_pressed()
		#print pos
		#print press

		color_play = green
		color_controls = green
		color_exit = green


		if pos[0] >= 75 and pos[0] <=(75 + 150) and pos[1]>=400 and pos[1] <= (400 + 50):
			color_play = light_green
			if press[0] == 1:
				return 1

		elif pos[0] >= 325 and pos[0] <=(325 + 150) and pos[1]>=400 and pos[1] <= (400 + 50):
			color_controls = light_green
			if press[0] == 1:
				return 2

		elif pos[0] >= 575 and pos[0] <=(575 + 150) and pos[1]>=400 and pos[1] <= (400 + 50):
			color_exit = light_green
			if press[0] == 1:
				return 3

		text1 = font_large.render("TANKS", True, red)
		gameDisplay.blit(text1, (230, 150))

		pygame.draw.rect(gameDisplay, color_play, (75, 400, 150, 50))
		text2 = font_medium.render("Play", True, white)
		gameDisplay.blit(text2, (110, 405))

		pygame.draw.rect(gameDisplay, color_controls, (325, 400, 150, 50))
		text3 = font_medium.render("Controls", True, white)
		gameDisplay.blit(text3, (330, 405))

		pygame.draw.rect(gameDisplay, color_exit, (575, 400, 150, 50))
		text4 = font_medium.render("Exit", True, white)
		gameDisplay.blit(text4, (610, 405))

		pygame.display.update()


val = menu()
if val == 1:
	gameloop()
elif val == 2:
	pass
#	val_controls = controls()
#	if val_controls == 1:
#		gameloop()
#	elif val_controls == 2:
#		pygame.quit()
#		quit()
elif val == 3:
	pygame.quit()
	quit()