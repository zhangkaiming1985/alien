import pygame.font


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

	def prep_score(self):
		"""渲染得分，并设置位置"""
		# 结合button类可以更好理解
		score_str = str(self.status.score)
		self.score_image = self.font.render(score_str, True,
			self.text_color, self.ai_settings.bg_color)
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.right = self.screen_rect.right - 20
		self.score_image_rect.top = 20

	def draw_score(self):
		"""显示记分板"""
		self.screen.blit(self.score_image, self.score_image_rect)