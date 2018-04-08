class Settings:
	"""存储《外星人入侵》的所有设置的类"""

	def __init__(self):
		"""初始化游戏设置"""
		# 屏幕设置
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		self.caption = 'Alien Invasion'

		# 飞船设置
		self.ship_speed_factor = 5
		self.ship_limit = 3

		# 子弹设置
		self.bullet_width = 500
		self.bullet_height = 15
		self.bullet_bgcolor = (60, 60, 60)
		self.bullet_speed_factor = 5
		self.bullet_allowed = 10 # 子弹最大数量

		# 外星人设置
		self.alien_speed_factor = 10
		self.fleet_drop_speed = 100 # 外星人群下降速度
		self.fleet_direction = 1 # 外星人群移动方向，1右，-1左


