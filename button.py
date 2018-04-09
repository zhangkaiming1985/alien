import pygame.font


class Button:
	"""自定义按钮类"""

	# 分两层，第一层为按钮的矩形区域，第二层为按钮文本
	def __init__(self, screen, msg):
		"""初始化按钮属性"""
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		# 设置按钮属性
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		# 文本字体为默认，字号48
		self.font = pygame.font.SysFont(None, 48)

		# 按钮矩形及屏幕居中位置
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# 标签文本渲染
		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""将文本渲染为图像，并使其在按钮上居中"""
		self.msg_image = self.font.render(msg, True, self.text_color,
		                                  self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""将按钮显示在屏幕上"""
		# 用颜色填充按钮，再绘制文本
		self.screen.fill(self.button_color, self.rect)  # 第一层
		self.screen.blit(self.msg_image, self.msg_image_rect)  # 第二层
