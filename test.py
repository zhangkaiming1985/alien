import pygame, sys


class Base:
	def __init__(self):
		print("it is base class.")


class Leaf(Base):
	def __init__(self):
		# Base.__init__(self)
		super().__init__()
		print("it is leaf class")

test = Leaf()

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen_color = (60, 60, 60)
rect_color = (200, 200, 200)
rect = pygame.Rect(100, 100, 50, 50)

image = pygame.image.load('images/ship.bmp')
image_rect = image.get_rect()
image_rect.x = 50
image_rect.y = 50

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		screen.fill(screen_color)
		pygame.draw.rect(screen, rect_color, rect)
		screen.blit(image, image_rect)
		pygame.display.flip()