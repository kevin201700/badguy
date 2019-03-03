#_main_.py - 打耗子
from math import *
import time
from sys import exit
import pygame

pygame.init()
pygame.display.set_caption("打耗子")

screen = pygame.display.set_mode((640, 480))
screen_pic = pygame.image.load("grass")
#screen_pic = pygame.transform.scale(screen_pic, (640, 480))

dule = pygame.image.load("dude")
dule = pygame.transform.flip(dule , False, True)

castle = pygame.image.load("castle")



dule = pygame.transform.rotate(dule , 0)

screen.blit(screen_pic, (0, 0))
screen.blit(castle, (30, 30))
screen.blit(castle, (30, 180))
screen.blit(castle, (30, 330))
screen.blit(dule, (100, 100))
pygame.display.update()

time.sleep(3)

dule = pygame.transform.rotate(dule , -30)

screen.blit(screen_pic, (0, 0))
screen.blit(castle, (30, 30))
screen.blit(castle, (30, 180))
screen.blit(castle, (30, 330))
screen.blit(dule, (100, 100))
pygame.display.update()


cat_x = 100
cat_y = 100
mouse_x = 201
mouse_y = 302
a = mouse_y -cat_y
b = mouse_x - cat_x
angle = atan(a / b)
angle = angle * 180 / 3.141592654
angle = 0 - angle

is_start = 1

while True:
	if is_start == 1:

		cat_x = 100
		cat_y = 100
		a = mouse_y - cat_y
		b = mouse_x - cat_x
		angle_old = angle
		angle = atan(a / b)
		angle = angle * 180 / 3.141592654
		angle = 0 - angle

		# angle = atan((mouse[1]-123)/(mouse[0]-132))#*180/3.14159265
		if angle_old == angle:
			dule = pygame.transform.rotate(dule , angle)
		mouse_x, mouse_y = pygame.mouse.get_pos()
		screen.blit(screen_pic, (0, 0))
		screen.blit(castle, (30, 30))
		screen.blit(castle, (30, 180))
		screen.blit(castle, (30, 330))
		screen.blit(dule, (100, 100))
		#time.sleep(1)
	elif is_start == 2:
		screen.bilt()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.update()
