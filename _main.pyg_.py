#_main.pyg_.py - 打耗子-Pygame
from math import *
import time
from sys import exit
import pygame
from random import randint

pygame.init()
pygame.display.set_caption("打耗子")

angle = 0

screen = pygame.display.set_mode((640, 480))
screen_pic = pygame.image.load("resource/images/grass.png")
screen_pic = pygame.transform.scale(screen_pic, (640, 480))

bullet = pygame.image.load("resource/images/bullet.png")
bullet_display = []
bullet_x = []
bullet_y = []
bullet_angle = []
bullet_run_no = []
bullet_x_start = []
bullet_y_start = []

pygame.mixer.music.load("resource/audio/moonlight.wav")

dule = pygame.image.load("resource/images/dude.png")
dule_display = pygame.image.load("resource/images/dude.png")

castle = pygame.image.load("resource/images/castle.png")


badguy = pygame.image.load("resource/images/badguy.png")
badguy_2 = pygame.image.load("resource/images/badguy2.png")
badguy_3 = pygame.image.load("resource/images/badguy3.png")
badguy_4 = pygame.image.load("resource/images/badguy4.png")
badguy_x = []
badguy_y = []
badguy_no = []

is_start = 1

time_us = 0

while True:
	if is_start == 1:
		time.sleep(0.01)
		time_us += 1
		if pygame.mixer.music.get_busy() == False:
			pygame.mixer.music.play()
		dule_display_xy = (123 - dule_display.get_rect().width / 2,
						   132 - dule_display.get_rect().height / 2)
		mouse = pygame.mouse.get_pos()
		screen.blit(screen_pic, (0, 0))
		screen.blit(castle, (30, 30))
		screen.blit(castle, (30, 180))
		screen.blit(castle, (30, 330))
		screen.blit(dule_display, dule_display_xy)#(100, 100))
		if time_us % 50 == 0:
			badguy_x.append(640)
			badguy_y.append(randint(0, 480))
			badguy_no.append(0)
		for i in range(len(badguy_x)):
			badguy_x[i] -= 5
			if badguy_no[i] < 4:
				badguy_no[i] += 1
			else:
				badguy_no[i] = 1
			if badguy_no[i] == 1:
				screen.blit(badguy, (badguy_x[i], badguy_y[i]))
			elif badguy_no[i] == 2:
				screen.blit(badguy_2, (badguy_x[i], badguy_y[i]))
			elif badguy_no[i] == 3:
				screen.blit(badguy_3, (badguy_x[i], badguy_y[i]))
			elif badguy_no[i] == 4:
				screen.blit(badguy_4, (badguy_x[i], badguy_y[i]))
#============================剑移动====================
		for i in range(len(bullet_x)):
			#bullet_x[i] += 5
			bullet_run_no[i] += 1
			bullet_x[i] = (cos(bullet_angle[i]) * (5 * bullet_run_no[i])) + bullet_x_start[i]#dule_display_xy[0]  # 宽
			bullet_y[i] = (sin(bullet_angle[i]) * (5 * bullet_run_no[i])) + bullet_y_start[i]#dule_display_xy[1]  # 长
			#print("num" + str(i) + "x" + str(bullet_x[i]) + "y" + str(bullet_y[i]))
			bullet_display[i] = pygame.transform.rotate(bullet, bullet_angle[i])
			screen.blit(bullet_display[i], (bullet_x[i], bullet_y[i]))
			if bullet_x[i] >= 640:
				del bullet_x[i]
				del bullet_y[i]
				del bullet_display[i]
				del bullet_angle[i]
				del bullet_run_no[i]
				del bullet_x_start[i]
				del bullet_y_start[i]
				break
		for i in range(len(bullet_x)):  # 拿到所有的子弹
			for j in range(len(badguy_x)):  # 拿到所有的老鼠
				if badguy_x[j] - 32 < bullet_x[i] < badguy_x[j] + 15:  # 子弹x坐标有没有老鼠x坐标范围内
					if badguy_y[j] - 17 < bullet_y[i] < badguy_y[j] + 36:  # 子弹x坐标有没有老鼠x坐标范围内
						del badguy_y[j]  # 退出循环
						del badguy_x[j]
						#del bullet_x[i]
						#del bullet_y[i]
						break




		if mouse[0] - 132 >= 5:
			angle = 0 - atan((mouse[1]-123)/(mouse[0]-132))*180/3.14159265
			#print("angle" + str(angle))
		dule_display = pygame.transform.rotate(dule, angle)
		#time.sleep(1)
	elif is_start == 2:
		screen.bilt
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
#=====================剑出现======================
		if event.type == pygame.MOUSEBUTTONDOWN:
			bullet_x.append(132)
			bullet_y.append(126)
			bullet_display.append(pygame.transform.rotate(bullet , angle))
			bullet_angle.append(angle)
			bullet_run_no.append(0)
			bullet_x_start.append(dule_display_xy[0])
			bullet_y_start.append(dule_display_xy[1])
	pygame.display.update()
