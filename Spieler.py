import pygame, sys
from pygame.locals import *


class Spieler(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.left = 250
		self.top = 350
				
		self.sprite_list = ([man1], listman, [man4], [man2], [man1])
		self.sprite_iterator = 0
		
		self.state = 0 #0 = stand, 1 = move, 2 = jump, 3 = fall, 4 = duck
		
		self.gravitation = 0
		self.jumpPower = 0
		self.jumpHeight = 37
		
		self.direction = 1
		
		self.canDoubleJump = True
		
	def rect(self):
		return pygame.Rect(self.left, self.top, self.current_sprite().get_width(), self.current_sprite().get_height())
	
	def base_rect(self):
		return pygame.Rect(self.left, self.top + self.current_sprite().get_height(), self.current_sprite().get_width(), 2)
	
	def current_sprite(self):
		return self.sprite_list[self.state][self.sprite_iterator]
		
	def rev_sprite_list(self):
		for i in range(len(self.sprite_list)):
			for j in range(len(self.sprite_list[i])):
				self.sprite_list[i][j] = pygame.transform.flip(self.sprite_list[i][j], True, False)
		
	def jump(self):
		if welt.isGrounded(self.base_rect()):
			self.jumpPower = 15
			
	def doubleJump(self):
		if self.canDoubleJump:
			self.raiseJumpPower(15)
			self.canDoubleJump = False
			
	def raiseJumpPower(self, amount):
		self.jumpPower = amount
		self.gravitation = 0
			
	def y_move(self):
		if self.jumpPower > 0:
			self.top -= 25
			self.jumpPower -= 1
			if self.jumpPower == 0:
				self.gravitation = 0
		if not welt.isGrounded(self.base_rect()):
			self.top += self.gravitation
			self.gravitation += 2
		else:
			if self.gravitation > 0:
				self.gravitation = 0
			self.jumpPower = 0
			
	def iterate(self):
		if self.sprite_iterator >= len(self.sprite_list[self.state]) -1:
			self.sprite_iterator = 0
		else:
			self.sprite_iterator += 1
			
	def beschleunigen(self):
		if welt.moveSpeed < 16 and self.state != 0:
			welt.moveSpeed += 1
		elif welt.moveSpeed > 1 and self.state == 0:
			welt.moveSpeed -= 2
				
			
	def selfblit(self):
		self.iterate()
		DISPLAYSURF.blit(self.current_sprite(), (self.left, self.top))
		
	def state_update(self):
		keys = pygame.key.get_pressed()
		if welt.isGrounded(self.base_rect()):
			self.canDoubleJump = True
			if keys[K_RIGHT] or keys[K_LEFT]:
				self.state = 1
			else:
				self.state = 0
				self.sprite_iterator = 0
		else:
			if self.jumpPower > 0:
				self.state = 2
				#if self.sprite_iterator > 1:
					#self.sprite_iterator = 0
				self.sprite_iterator = 0
			else:
				self.state = 3
				self.sprite_iterator = 0
		if keys[K_RIGHT] and not keys[K_LEFT]:
			if self.direction == -1:
				self.direction = 1
				self.rev_sprite_list()
		elif not keys[K_RIGHT] and keys[K_LEFT]:
			if self.direction == 1:
				self.direction = -1
				self.rev_sprite_list()
				
	def kill(self):
		pygame.quit()
		sys.exit()
			
		
	def update(self):
		#print(self.state)
		#print(self.top)
		#print(self.sprite_iterator)
		#print(self.canDoubleJump)
		self.state_update()
		self.y_move()
		self.selfblit()
		self.beschleunigen()
		#print(self.jumpPower)
		#print(self.direction)
			
			
class Welt():
	def __init__(self, bloecke, gegner, spieler):
		self.bloecke = bloecke
		self.spieler = spieler
		self.moveSpeed = 1
		self.maxMoveSpeed = 12
		self.gegner = gegner
		
	def isGrounded(self, rect):
		for i in self.bloecke:
			if i.colliderect(rect):
				self.spieler.top = i.top - self.spieler.current_sprite().get_height()
				self.spieler.gravitation = 0
				return True
		return False
		
	def move(self):
		for i in self.bloecke:
			i.left -= self.moveSpeed * self.spieler.direction
			if self.spieler.state == 2 or self.spieler.state == 3:
				i.left -= 4 * self.spieler.direction
		for j in self.gegner:
			j.left -= self.moveSpeed * self.spieler.direction
			if self.spieler.state == 2 or self.spieler.state == 3:
				j.left -= 4 * self.spieler.direction
			j.start -= self.moveSpeed * self.spieler.direction
			if self.spieler.state == 2 or self.spieler.state == 3:
				j.start -= 4 * self.spieler.direction
			j.ende -= self.moveSpeed * self.spieler.direction
			if self.spieler.state == 2 or self.spieler.state == 3:
				j.ende -= 4 * self.spieler.direction
		
		
	def update(self):			
		for i in self.bloecke:
			DISPLAYSURF.blit(pygame.Surface((i.width, i.height)), (i.left, i.top))
		for j in self.gegner:
			j.update()
			if self.spieler.base_rect().colliderect(j.headRect()):
				self.spieler.raiseJumpPower(15)
				j.kill()
			elif self.spieler.rect().colliderect(j.bodyRect()):
				self.spieler.kill()
		self.spieler.update()
		pygame.display.update()
		

		
class Feind(pygame.sprite.Sprite):
	def __init__(self, top,  start, ende, sprites, speed, lebenspunkte):
		pygame.sprite.Sprite.__init__(self)
		self.start = start
		self.ende = ende
		self.left = start
		self.top = top
		self.sprites = sprites
		self.speed = speed
		self.lebenspunkte = lebenspunkte
		self.isLebendig = True
		self.direction = 'right'
		
		self.sprite_iterator = 0
		
	def current_sprite(self):
		if self.sprite_iterator >= len(self.sprites):
			self.sprite_iterator = 0
		return self.sprites[self.sprite_iterator]
		
	def headRect(self):
		return pygame.Rect(self.left - 10, self.top - 10, self.current_sprite().get_width() + 20, 20)
		
	def bodyRect(self):
		return pygame.Rect(self.left + 5, self.top + 20, self.current_sprite().get_width() - 10, self.current_sprite().get_height() - 20)
	
	def rev_sprite_list(self):
		for i in range(len(self.sprites)):
			self.sprites[i] = pygame.transform.flip(self.sprites[i], True, False)
			
	def update(self):
		if self.sprite_iterator >= len(self.sprites):
			self.sprite_iterator = 0
		DISPLAYSURF.blit(self.sprites[self.sprite_iterator], (self.left, self.top))
		self.sprite_iterator += 1
		if self.direction == 'right':
			if self.left < self.ende:
				self.left += self.speed
			else:
				self.direction = 'left'
				self.rev_sprite_list()
		elif self.direction == 'left':
			if self.left > self.start:
				self.left -= self.speed
			else:
				self.direction = 'right'
				self.rev_sprite_list()
		#print(self.left)
		
	def kill(self):
		pass
		
		
		
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1600, 1200))
man1 = pygame.image.load("man1.png")
man2 = pygame.image.load("man2.png")
man3 = pygame.image.load("man3.png")
man4 = pygame.image.load("man4.png")
man1r = pygame.image.load("man1r.png")
man2r = pygame.image.load("man2r.png")
man3r = pygame.image.load("man3r.png")
man4r = pygame.image.load("man4r.png")
listman2 = [man1, man2, man3, man4]
listman = [man1, man2, man3, man4]
listmanr = [man1r, man2r, man3r, man4r]

block1 = pygame.Rect(50, 550, 250, 40)
block2 = pygame.Rect(650, 550, 100, 40)
block3 = pygame.Rect(1000, 400, 400, 30)
block4 = pygame.Rect(1200, 700, 150, 30)
block5 = pygame.Rect(1600, 400, 200, 50)
block6 = pygame.Rect(2500, 550, 100, 30)
block7 = pygame.Rect(2900, 300, 100, 30)
block8 = pygame.Rect(3400, 200, 100, 30)
block9 = pygame.Rect(3700, 0, 100, 30)
block10 = pygame.Rect(4200, -150, 100, 30)

g1 = Feind(block3.top - man1.get_height(),950, 1350 - man1.get_width(), listman2, 5, 3)

clock = pygame.time.Clock()
fps = 20

spieler = Spieler()

welt = Welt([block1, block2, block3, block4, block5, block6, block7, block8, block9, block10] , [g1], spieler)

def main():
	
	while True:
		DISPLAYSURF.fill((255, 255, 255))
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE and not welt.isGrounded(spieler.base_rect()) and spieler.jumpPower <= 13:
					spieler.doubleJump()
		if keys[K_SPACE]:
			spieler.jump()
		if keys[K_RIGHT] or keys[K_LEFT]:
			welt.move()
		welt.update()
		clock.tick(fps)
			
main()
						
			
