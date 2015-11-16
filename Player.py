import pygame
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
	def __init__(self, img_list, left, top, moveSpeed, jumpPower, clock, source, isMoving=True, isColliding=False, isGrounded = True):
		pygame.sprite.Sprite.__init__(self)
		self.img_list = img_list
		self.moveSpeed = moveSpeed
		self.isMoving = isMoving
		self.jumpPower = jumpPower
		self.isColliding = isColliding
		self.isGrounded = isGrounded
		self.surf = pygame.Surface((img_list[0].get_width(), img_list[0].get_height()))
		self.rect = pygame.Rect(left, top, self.surf.get_width(), self.surf.get_height())
		self.clock = clock
		self.source = source
		self.i = 0

		
	def move(self, direction):
		if not self.isColliding:
			if direction == 'right':
				self.rect.right += self.moveSpeed
			elif direction == 'left':
				self.rect.right -= self.moveSpeed
				
	def jump(self):
		if self.isGrounded:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_UP]:
				self.rect.top -= self.jumpPower
			
			
	def update(self, ground, platform_list):
		for i in pygame.sprite.Group.sprites(ground):
			if pygame.sprite.collide_rect(self, i):
				self.isGrounded = True
				break
			else:
				self.isGrounded = False
		if not self.isGrounded:
			self.rect.top += 10 #Gravitation
		keys = pygame.key.get_pressed()
		if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
			self.isMoving = False
			self.surf.fill(BLACK)
			self.i = 0
		else:
			self.isMoving = True
		if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
			self.move('right')
		if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
			self.move('left')
		if keys[pygame.K_UP]:
			self.jump()
		self.selfblit("des")
			
	def selfblit(self, direction):
		if not self.isMoving:
			self.surf.blit(self.img_list[0], (0,0))
			self.source.blit(self.surf, (self.rect.left, self.rect.top))
		else:
			self.surf.fill(BLACK)
			self.surf.blit(self.img_list[self.i], (0,0))
			self.source.blit(self.surf, (self.rect.left, self.rect.top))
			self.clock.tick(30)
			self.i += 1
			if self.i >= len(self.img_list):
				self.i = 0

	