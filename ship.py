import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
	"""飞船类"""
	def __init__(self, screen, ai_settings):
		super().__init__()
		"""初始化飞船位置"""
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载飞船图像并获取飞船和屏幕的外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 设置飞船矩形中点x坐标为屏幕矩形中点x坐标，飞船底部为屏幕底部
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 将飞船center值存储为float
		self.center = float(self.rect.centerx)

		# 移动标志
		self.moving_right = False
		self.moving_left = False


	def blitme(self):
		# 绘制飞船
		self.screen.blit(self.image, self.rect)

	def update(self):
		# 根据移动标志调整飞船位置
		# 由于rect只能存储整数部分，为精确飞船位置，改为更新飞船的center值，然后传给rect
		# 防止飞船飞离屏幕
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center

	def center_ship(self):
		"""重置飞船位置"""
		self.rect.centerx = self.screen_rect.centerx