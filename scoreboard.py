import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scroeboard:
	"""记分板类，显示玩家当前得分、最高分、等级、余下飞船数量"""
	def __init__(self, screen, ai_settings, status):
		"""初始化记分板属性"""
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.status = status
		self.ai_settings = ai_settings

		# 字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# 得分
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ship()

	def prep_score(self):
		"""将得分转化为渲染为图像"""
		# 结合button类可以更好理解
		rounded_score = int(round(self.status.score, -1)) # 取10的整数倍
		score_str = "{:,}".format(rounded_score) # 添加千分位
		self.score_image = self.font.render(score_str, True,
			self.text_color, self.ai_settings.bg_color)
		# 获取矩形，设置位置
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.right = self.screen_rect.right - 20
		self.score_image_rect.top = 20

	def prep_high_score(self):
		"""将最高分渲染为图像"""
		rounded_high_score = int(round(self.status.high_score, -1))
		high_score_str = "{:,}".format(rounded_high_score)
		self.high_score_image = self.font.render(high_score_str,
			True, self.text_color, self.ai_settings.bg_color)
		# 获取矩形，设置位置
		self.high_score_image_rect = self.high_score_image.get_rect()
		self.high_score_image_rect.centerx = self.screen_rect.centerx
		self.high_score_image_rect.top = 20

	def prep_level(self):
		"""将目前等级渲染为图像"""
		level_str = str(self.status.level)
		self.level_image = self.font.render(level_str, True,
			self.text_color, self.ai_settings.bg_color)
		# 获取矩形，设置位置
		self.level_image_rect = self.level_image.get_rect()
		self.level_image_rect.right = self.score_image_rect.right
		self.level_image_rect.top = self.score_image_rect.bottom + 10

	def prep_ship(self):
		"""将飞船个数图像渲染"""
		# 创建飞船精灵组，然后根据将飞船存入组中
		self.ships = Group()
		for ship_number in range(self.status.ship_left):
			ship = Ship(self.screen, self.ai_settings)
			ship.rect.top = self.screen_rect.top + 20
			ship.rect.left = 10 + ship_number * ship.rect.width
			self.ships.add(ship)


	def draw_score(self):
		"""显示记分板"""
		self.screen.blit(self.score_image, self.score_image_rect)
		self.screen.blit(self.high_score_image, self.high_score_image_rect)
		self.screen.blit(self.level_image, self.level_image_rect)
		self.ships.draw(self.screen)