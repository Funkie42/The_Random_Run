import pygame
from pygame.locals import *
			

class Ground(pygame.sprite.Group):
	def __init__(self, platform_list, background, source):
		pygame.sprite.Group.__init__(self)
		right_mom = 0
		for i in range(len(platform_list)):
			self.add(Platform(right_mom, source.get_height() - platform_list[i][1], platform_list[i][0], platform_list[i][1], background, source))
			right_mom = right_mom + platform_list[i][0]		
			
	def selfblit(self):
		for i in pygame.sprite.Group.sprites(self):
			i.selfblit()
			
		
		
class Platform(pygame.sprite.Sprite):
	def __init__(self, left, top, width, height, background, source):
		pygame.sprite.Sprite.__init__(self)
		self.background = background
		self.surf = pygame.Surface((width, height))
		self.rect = pygame.Rect(left, top, width, height)
		self.source = source
		self.selfblit()
		
	def selfblit(self):
		for y in range(0, self.surf.get_height(), self.background.get_height()):
			for x in range(0, self.surf.get_width(), self.background.get_width()):
				self.surf.blit(self.background, (x, y))
		self.source.blit(self.surf, (self.rect.left, self.rect.top))

			