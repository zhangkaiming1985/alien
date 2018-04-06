class Settings:
	"""存储《外星人入侵》的所有设置的类"""

	def __init__(self):
		"""初始化游戏设置"""
		# 屏幕设置
		self.screen_width = 800
		self.screen_heigth = 600
		self.bg_color = (230, 230, 230)
		self.caption = 'Alien Invasion'

		# 飞船设置
		self.ship_speed_factor = 5

		# 子弹设置
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_bgcolor = (60, 60, 60)
		self.bullet_speed_factor = 3
		self.bullet_allowed = 10 # 子弹最大数量
