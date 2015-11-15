import pygame
from pygame.locals import *
			

class Ground(list):
	def __init__(self, platform_list, background, source):
		super().__init__()
		right_mom = 0
		for i in range(0, len(platform_list)):
			print(right_mom)
			self.insert(i, Platform(platform_list[i][0], platform_list[i][1], right_mom, 600 - platform_list[i][1], background, source))
			right_mom = right_mom + platform_list[i][0]
		
		
class Platform(pygame.sprite.Sprite):
	def __init__(self, width, height, top, left, background, source):
		super().__init__()
		self.background = background
		self.top = top
		self.left = left
		self.surf = pygame.Surface((width, height))
		self.rect = pygame.Rect(width, height, top, left)
		self.source = source
		self.selfblit()
		
	def selfblit(self):
		for y in range(0, self.surf.get_height(), self.background.get_height()):
			for x in range(0, self.surf.get_width(), self.background.get_width()):
				self.surf.blit(self.background, (x, y))
		self.source.blit(self.surf, (self.top, self.left))

			