Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: D:\Work\Coding\Python3\打耗子\Code\_main_.py =============
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "D:\Work\Coding\Python3\打耗子\Code\_main_.py", line 26, in <module>
    angle = atan((mouse[2]-123)/(mouse[1]-132))*180/3.14159265
IndexError: tuple index out of range
>>> pigame.quit()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    pigame.quit()
NameError: name 'pigame' is not defined
>>> pygame.quit
<built-in function quit>
>>> pygame.quit
<built-in function quit>
>>> mouse
(639, 479)
>>> mouse[1]
479
>>> 2
2
>>> mouse[2]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    mouse[2]
IndexError: tuple index out of range
>>> 
============= RESTART: D:\Work\Coding\Python3\打耗子\Code\_main_.py =============
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
>>> angle
-15.319884080522039
>>> 
============= RESTART: D:\Work\Coding\Python3\打耗子\Code\_main_.py =============
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
>>> angle
-13.736268321318546
>>> angle2
-76.26373178152146
>>> 
============= RESTART: D:\Work\Coding\Python3\打耗子\Code\_main_.py =============
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "D:\Work\Coding\Python3\打耗子\Code\_main_.py", line 28, in <module>
    dule = pygame.transform.rotate(dule , angle)
pygame.error: Width or height is too large
>>> 
=============================== RESTART: Shell ===============================
>>> #_main_.py - 打耗子
from math import *
from sys import exit
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
screen_pic = pygame.image.load("grass")
screen_pic = pygame.transform.scale(screen_pic, (640, 480))

dule = pygame.image.load("dude")
dule = pygame.transform.flip(dule , True, False)

castle = pygame.image.load("castle")

is_start = 1

while True:
	if is_start == 1:
		mouse = pygame.mouse.get_pos()
		screen.blit(screen_pic, (0, 0))
		screen.blit(castle, (30, 30))
		screen.blit(castle, (30, 180))
		screen.blit(castle, (30, 330))
		screen.blit(dule, (100, 100))
		angle = atan((mouse[1]-123)/(mouse[0]-132))*180/3.14159265
		dule = pygame.transform.rotate(dule , angle)
	elif is_start == 2:
		screen.bilt
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.update()

SyntaxError: multiple statements found while compiling a single statement
>>> 
#_main_.py - 打耗子
from math import *
from sys import exit
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
screen_pic = pygame.image.load("grass")
screen_pic = pygame.transform.scale(screen_pic, (640, 480))

dule = pygame.image.load("dude")
dule = pygame.transform.flip(dule , True, False)

castle = pygame.image.load("castle")

is_start = 1

while True:
	if is_start == 1:
		mouse = pygame.mouse.get_pos()
		screen.blit(screen_pic, (0, 0))
		screen.blit(castle, (30, 30))
		screen.blit(castle, (30, 180))
		screen.blit(castle, (30, 330))
		screen.blit(dule, (100, 100))
		angle = atan((mouse[1]-123)/(mouse[0]-132))*180/3.14159265
		dule = pygame.transform.rotate(dule , angle)
	elif is_start == 2:
		screen.bilt
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.update()

SyntaxError: multiple statements found while compiling a single statement
>>> from math import *
from sys import exit
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
screen_pic = pygame.image.load("grass")
screen_pic = pygame.transform.scale(screen_pic, (640, 480))

dule = pygame.image.load("dude")
dule = pygame.transform.flip(dule , True, False)

castle = pygame.image.load("castle")

is_start = 1

while True:
	if is_start == 1:
		mouse = pygame.mouse.get_pos()
		screen.blit(screen_pic, (0, 0))
		screen.blit(castle, (30, 30))
		screen.blit(castle, (30, 180))
		screen.blit(castle, (30, 330))
		screen.blit(dule, (100, 100))
		angle = atan((mouse[1]-123)/(mouse[0]-132))*180/3.14159265
		dule = pygame.transform.rotate(dule , angle)
	elif is_start == 2:
		screen.bilt
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.update()

SyntaxError: multiple statements found while compiling a single statement
>>> 
from math import *
from sys import exit
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
screen_pic = pygame.image.load("grass")
screen_pic = pygame.transform.scale(screen_pic, (640, 480))

dule = pygame.image.load("dude")
dule = pygame.transform.flip(dule , True, False)

castle = pygame.image.load("castle")

is_start = 1

while True:
	if is_start == 1:
		mouse = pygame.mouse.get_pos()
		screen.blit(screen_pic, (0, 0))
		screen.blit(castle, (30, 30))
		screen.blit(castle, (30, 180))
		screen.blit(castle, (30, 330))
		screen.blit(dule, (100, 100))
		angle = atan((mouse[1]-123)/(mouse[0]-132))*180/3.14159265
		dule = pygame.transform.rotate(dule , angle)
	elif is_start == 2:
		screen.bilt
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.update()

SyntaxError: multiple statements found while compiling a single statement
>>> 
============= RESTART: D:\Work\Coding\Python3\打耗子\Code\_main_.py =============
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "D:\Work\Coding\Python3\打耗子\Code\_main_.py", line 28, in <module>
    dule = pygame.transform.rotate(dule , angle)
pygame.error: Width or height is too large
>>> 
============= RESTART: D:\Work\Coding\Python3\打耗子\Code\_main_.py =============
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "D:\Work\Coding\Python3\打耗子\Code\_main_.py", line 30, in <module>
    time.sleep(1000000000000000)
OverflowError: timestamp too large to convert to C _PyTime_t
>>> 
============= RESTART: D:\Work\Coding\Python3\打耗子\Code\_main_.py =============
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html

============= RESTART: D:\Work\Coding\Python3\打耗子\Code\_main_.py =============
pygame 1.9.4
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "D:\Work\Coding\Python3\打耗子\Code\_main_.py", line 29, in <module>
    dule = pygame.transform.rotate(dule , 0 - angle)
pygame.error: Width or height is too large
>>> pygame.quit()
>>> 
