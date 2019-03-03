import pygame
from pygame.locals import *
import math   # 因为需要计算旋转的角度
import random # 因为需要用到随机的功能
import time


# 初始化pygame，设置展示窗口
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 加载图片
player_img = pygame.image.load("resource/images/dude.png")
# 再加一些风景~
grass_img = pygame.image.load("resource/images/grass.png")
castle_img = pygame.image.load("resource/images/castle.png")
# 加载箭头
arrow_img = pygame.image.load('resource/images/bullet.png')
# 加载獾
badguy_img1 = pygame.image.load("resource/images/badguy.png")
badguy_img = badguy_img1

# 跟踪箭头
arrows = []
arrow_speed = 10

tick_ms = 0
playerpos = [100, 30]
angle = 0
angle_changed = True
# running = True
while True:
  time.sleep(0.01)
  tick_ms += 10

  position_mouse = pygame.mouse.get_pos()
  angle_n = math.atan2(position_mouse[1]-playerpos[1], position_mouse[0]-playerpos[0]) * 180/3.14159265
  angle_n *= -1
  if angle_n != angle:
    angle = angle_n
    angle_changed = True

      # 在给屏幕画任何东西之前用黑色进行填充
  screen.fill(0)
      # 添加的背景也需要画在屏幕上
  for x in range(width//grass_img.get_width()+1):
    for y in range(height//grass_img.get_height()+1):
      screen.blit(grass_img, (x*100, y*100))
  screen.blit(castle_img, (0, 30))
  screen.blit(castle_img, (0, 135))
  screen.blit(castle_img, (0, 240))
  screen.blit(castle_img, (0, 345))

  playerrot = pygame.transform.rotate(player_img, angle)
  playerpos_r = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
  #screen.blit(playerrot, playerpos)
  screen.blit(playerrot, playerpos_r)

  arrow_index = 0
  for arrow in arrows:
    arrow[1] += arrow_speed
    arrow_rot = pygame.transform.rotate(arrow_img, arrow[0])
    arrow_move = [arrow[1]*math.cos(math.radians(-arrow[0])), arrow[1]*math.sin(math.radians(-arrow[0]))]
    arrow_xy = (playerpos[0]+arrow_move[0]-arrow_rot.get_rect().width/2, playerpos[1]+arrow_move[1]-arrow_rot.get_rect().height/2)
    screen.blit(arrow_rot, arrow_xy)


  pygame.display.update()

  if angle_changed:
    angle_changed = False
    # print("width: ", playerrot.get_rect().width, ",    height: ", playerrot.get_rect().height, "    angle: ", angle)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      arrows.append([angle, 0])

