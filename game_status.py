class GameStatus:
	"""游戏信息统计类"""

	def __init__(self, ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		# 游戏开始时处于非活动状态
		self.game_active = False
		self.reset_status()

	def reset_status(self):
		"""初始化在游戏运行期间，可能发生变化的信息"""
		# 飞船剩余个数，初始值在setting中设置
		self.ship_left = self.ai_settings.ship_limit
		# 玩家得分
		self.score = 0
