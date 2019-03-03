import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 1000))
angle = 0

image = pygame.image.load("dude")
image2 = pygame.image.load("dude")
bg = pygame.image.load("grass")
bg = pygame.transform.scale(bg, (1500, 1000))



while True:
	screen.blit(bg, (0, 0))
	#mouse = pygame.mouse.get_pos()
	mouse = [100, 100]
	screen.blit(image2, mouse)
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				angle += 10
				image2 = pygame.transform.rotate(image, angle)
			elif event.key == pygame.K_RIGHT:
				angle -= 10
				image2 = pygame.transform.rotate(image, angle)
			elif event.key == pygame.K_UP:
				mouse = (mouse[0], mouse[1]+100)
			elif event.key == pygame.K_DOWN:
				mouse = (mouse[0]+100, mouse[1])
