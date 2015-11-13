import pygame
from pygame.locals import *

class Ground():
	def __init__(self, coordinaten_liste, background):
		self.coordinaten_liste = coordinaten_liste #liste von Koordinaten
		self.background = background
		self.moment_right = 0
		
		
	def selfblit(self, source):
		for i in range(len(self.coordinaten_liste)):
			surf = pygame.Surface((self.coordinaten_liste[i][0], self.coordinaten_liste[i][1]))
			for y in range(0, surf.get_height(), self.background.get_height()):
				for x in range(0, surf.get_width(), self.background.get_width()):
					surf.blit(self.background, (x, y))
			source.blit(surf, (self.moment_right, 600 - self.coordinaten_liste[i][1]))
			rect = surf.get_rect()
			self.moment_right = self.moment_right +  rect.right
			
			

class Platform(pygame.Surface):
	def __init__(self, width, height, top, left , background):
		super().__init__((width, height))
		self.top = top
		self.left = left
		self.background = background
		
	def selfblit(self, source):
		for y in range(0, self.get_height(), self.background.get_height()):
				for x in range(0, self.get_width(), self.background.get_width()):
					self.blit(self.background, (x, y))
		source.blit(self, (self.top, self.left))

			