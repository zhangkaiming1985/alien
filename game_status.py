class GameStatus:
	"""游戏信息统计类"""

	def __init__(self, ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		self.reset_status()


	def reset_status(self):
		"""初始化在游戏运行期间，可能发生变化的信息"""
		self.ship_left = self.ai_settings.ship_limit
