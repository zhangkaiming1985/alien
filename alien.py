import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""外星人类"""

	def __init__(self, screen, ai_settings):
		"""初始化外星人和起始位置"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载外星人图像，获得外界矩形
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# 设置外星人起始位置
		# 屏幕左上坐标0，0，下面用外星人矩形长宽值设置了初始位置
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 用小数存储外星人位置
		self.x = float(self.rect.x)

		# 外星人速度
		self.speed_factor = ai_settings.alien_speed_factor

	def blitme(self):
		# 绘制外星人
		self.screen.blit(self.image, self.rect)

	def update(self):
		# 向左右移动外星人，并防止精度损失
		self.x = float(self.rect.x)
		self.x += (self.speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		# 检查外星人个体是否到达屏幕边缘，若是返回Ture
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= screen_rect.left:
			return True

	def check_bottom(self):
		"""检查外星人个体是否到达屏幕底端，若是返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom:
			return True