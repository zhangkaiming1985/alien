import pygame


class Ship:
	"""存储飞船设置"""

	def __init__(self, screen):
		"""初始化飞船初始位置"""
		self.screen = screen

		# 加载飞船图像并获取飞船和屏幕的外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 设置飞船矩形中点x坐标为屏幕矩形中点x坐标，飞船底部为屏幕底部
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		self.screen.blit(self.image, self.rect)
