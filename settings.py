class Settings:
	"""存储《外星人入侵》的所有设置的类"""

	def __init__(self):
		"""初始化游戏设置"""
		# 静态数据
		# 屏幕设置
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		self.caption = 'Alien Invasion'

		# 飞船设置
		self.ship_limit = 3

		# 子弹设置
		self.bullet_width = 500
		self.bullet_height = 15
		self.bullet_bgcolor = (60, 60, 60)
		self.bullet_allowed = 10 # 子弹最大数量

		# 外星人设置
		self.fleet_drop_speed = 50 # 外星人群下降速度

		# 提升难度比例
		self.speedup_scale = 2
		self.score_scale = 1.8

		# 动态数据
		# 初始化动态数据
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""初始化动态数据"""
		# 飞船速度
		self.ship_speed_factor = 3
		# 子弹速度
		self.bullet_speed_factor = 5
		# 外星人速度
		self.alien_speed_factor = 3
		# 外星人移动方向，1右，-1左
		self.fleet_direction = 1
		# 外星人分数
		self.alien_points = 50

	def increase_speed(self):
		"""增加游戏难度"""
		# 提高飞船速度
		self.ship_speed_factor *= self.speedup_scale
		# 提高外星人速度
		self.alien_speed_factor *= self.speedup_scale
		# 提高子弹速度
		self.bullet_speed_factor *= self.speedup_scale
		# 提高外星人分数
		self.alien_points *= self.score_scale



