import pygame
from pygame.locals import *
pygame.init()

width, height=320, 240
tela=pygame.display.set_mode((width, height), pygame.SCALED | pygame.FULLSCREEN)

class player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.run=[
		pygame.image.load("madeline/run/1.png").convert_alpha(),
		pygame.image.load("madeline/run/2.png").convert_alpha(),
		pygame.image.load("madeline/run/3.png").convert_alpha(),
		pygame.image.load("madeline/run/4.png").convert_alpha(),
		pygame.image.load("madeline/run/5.png").convert_alpha(),
		pygame.image.load("madeline/run/6.png").convert_alpha(),
		pygame.image.load("madeline/run/7.png").convert_alpha(),
		pygame.image.load("madeline/run/8.png").convert_alpha()
		]
		self.t=0
		self.s=0
		
		self.image=self.run[self.s]
		self.rect=self.image.get_rect()
		
		self.rect[0]=width/2-self.rect[2]/2
		self.rect[1]=height/2-self.rect[3]/2
	def update(self):
		self.t+=dt
		if self.t>=0.1:
			self.s=(self.s+1)%8
			self.image=self.run[self.s]
			
			self.t=0

players=pygame.sprite.Group()
p=player()
players.add(p)

dt=0
t=0
while True:
	for event in pygame.event.get():
		if event.type=="QUIT":
			break
	tela.fill((25, 25, 25))
	
	players.draw(tela)
	players.update()
	
	dt=(pygame.time.get_ticks()-t)/1000.0
	t=pygame.time.get_ticks()
		
	pygame.display.flip()