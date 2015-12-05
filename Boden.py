import pygame, sys, pymunk
from pygame.locals import*

class Boden(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
class Block(Boden):
	def __init__(self, rect, sprite):
		self.rect = rect
		self.sprite = sprite
		self.surf = pygame.Surface((self.rect.width, self.rect.height))
		self.body = pymunk.Body()
		self.body.position = self.rect.center
		self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))
		self.shape.collision_type = 2
		
		
	def center_rect(self):
		x = self.rect
		x.center = self.body.position
		return x
		
	def update(self):
		for i in range(0, self.surf.get_height(), self.sprite.get_height()):
			for j in range(0, self.surf.get_width(), self.sprite.get_width()):
				self.surf.blit(self.sprite, (j,i))
		self.shape.cache_bb()
		
