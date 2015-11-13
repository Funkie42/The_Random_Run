import pygame
from pygame.locals import *

class platform():
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
			print(self.moment_right)
			self.moment_right = self.moment_right +  rect.right
	
			