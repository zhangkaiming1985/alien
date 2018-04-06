import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""子弹类"""

	def __init__(self, screen, ai_settings, ship):
		"""初始化子弹位置，在飞船上方"""
		# 初始化父类
		super().__init__()
		self.screen = screen

		# 在0，0位置初始化子弹
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
			ai_settings.bullet_height)
		# 将子弹移动到飞船上方
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		# 用小数存储子弹纵轴位置
		self.y = float(self.rect.y)
		# 设置子弹颜色和速度
		self.color = ai_settings.bullet_bgcolor
		self.speed_factor = ai_settings.bullet_speed_factor

	def draw_bullet(self):
		# 绘制子弹
		pygame.draw.rect(self.screen, self.color, self.rect)

	def update(self):
		# 向上移动子弹,先获得小数，再传给rect获得整数
		self.y -= self.speed_factor
		self.rect.y = self.y