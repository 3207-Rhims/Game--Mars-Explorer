
import math, random, sys
import pygame
from pygame.locals import *
import time

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface			
W, H = 1280,620
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Surviving In Mars")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

bg = pygame.image.load("/Users/Arafat/Desktop/himel/hellow world.cpp/himel.py/nasa game/img/level-1.png").convert()
bgWidth, bgHeight = bg.get_rect().size

stageWidth = bgWidth * 2
stagePosX = 0

startScrollingPosX = HW

circleRadius = 10
circlePosX = circleRadius
playerImg=pygame.image.load("/Users/Arafat/Desktop/himel/hellow world.cpp/himel.py/nasa game/spaceship.png").convert()
playerPosX = circleRadius
playerPosY = 385
playerVelocityX = 0

font=pygame.font.SysFont(None,25)
def message(msg,color):
    screen_text=font.render(msg,True,color)
    DS.blit(screen_text, [int(W/10),int(H/15)])
    

def player(playerPosX,playerPosY):
    playerVelocityX = 0
    DS.blit(playerImg, (playerPosX,playerPosY))

# main loop
while True:
	events()

	k = pygame.key.get_pressed()
	
	if k[K_RIGHT]:
		playerVelocityX = 1
	elif k[K_LEFT]:
		playerVelocityX = -1
	else:
		playerVelocityX = 0
		
	playerPosX += playerVelocityX
	if playerPosX > stageWidth - circleRadius: playerPosX = stageWidth - circleRadius
	if playerPosX < circleRadius: playerPosX = circleRadius
	if playerPosX < startScrollingPosX: circlePosX = playerPosX
	elif playerPosX > stageWidth - startScrollingPosX: circlePosX = playerPosX - stageWidth + W
	else:
		circlePosX = startScrollingPosX
		stagePosX += -playerVelocityX
	
	rel_x = stagePosX % bgWidth
	DS.blit(bg, (rel_x - bgWidth, 0))
	if rel_x < W:
		DS.blit(bg, (rel_x, 0))
    
	stagePosX-=1
	DS.blit(playerImg, (int(circlePosX), int(playerPosY) - 25))
	
	if k[K_CAPSLOCK]:
		message("enter explosion for press a", BLACK) 
    #level-2
	if k[K_a]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-2.png").convert()
		bg=exp
		#if k[K_RIGHT]:
        		#message("new mars for press b", BLACK)     
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("New mars and for next level info press b", WHITE) 		
		pygame.display.update()  
    #level-3               
	if k[K_b]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-3.png").convert()
		bg=exp   
		#message("Wanna Plant some trees and want to mars too healthy for survive ? Press:C for YES OR Press:b for NO", BLACK)    
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("""Wanna Plant some trees? 
          press:C for YES OR Press:b for NO""", BLACK)  
		
		pygame.display.update()	
  	#level-4
	if k[K_c]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-4.png").convert()
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Wanna build a home?..Press D//for next level info push D 3sec",BLACK)
		pygame.display.update()  
	if k[K_d]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-5.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Wanna build a city?..Press E//for next level info push E 3sec",BLACK)
		pygame.display.update()   
	if k[K_e]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-6.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Its time to build some factory gather next level info // Press F...for next level info push F 3sec",BLACK)
		pygame.display.update()          
	if k[K_f]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-7.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("TOO much pollution? gather next level info PRESS G",BLACK)
		pygame.display.update() 
	if k[K_g]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-8.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("OMG!!!Flood,climate change for too much pollution,need to plant!!!! Press H ",BLACK)
		pygame.display.update()  
	if k[K_h]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-9.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Build renweable enrgy,PRESS (i) or grow farming for food,PRESS(k) ...for next level info push i/j 3sec",BLACK)
		pygame.display.update()  
	if k[K_i]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-10.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Build  renewable industry PRESS (j)... for next level info push K 3sec",BLACK)
		pygame.display.update()  
	if k[K_j]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-12.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Growing more harvest using science for ,PRESS(l) ...for next level info push i/j 3sec",BLACK)
		pygame.display.update()   
	if k[K_k]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-11.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Shortage of food , need food ,PRESS(j)  ...for next level info push i/j 3sec",BLACK)
		pygame.display.update()     
	if k[K_l]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-13.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Need some energy for modern life ,PRESS(i) OR PRESS (M) for more food using advance fertilizer ...for next level info push i 3sec",BLACK)
		pygame.display.update()   
	if k[K_m]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-16.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("mars are destroyed by chemical of agriculture produced ,PRESS(m) ...for next level info push n 3sec",BLACK)
		pygame.display.update() 
	if k[K_n]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-14.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Huge storm come,everything destroying ,PRESS(n) ...for next level info push o 3sec",WHITE)
		pygame.display.update() 
	if k[K_o]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-15.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("Big Bang come,time to go begining ,PRESS(o) ...for next level info push p 3sec",WHITE)
		pygame.display.update()
	if k[K_p]:
		exp=pygame.image.load("/Users/Arafat/Desktop\himel/hellow world.cpp/himel.py/nasa game/img/level-17.png").convert()   
		bg=exp
		DS.blit(bg, (rel_x,0))			   
		pygame.time.wait(10)
		message("GAME OVERRRRRRRRRRRR and we are now in begining",WHITE)
		pygame.display.update()      
        				        		        
	pygame.display.update()
 
	CLOCK.tick(FPS)
	DS.fill(BLACK)