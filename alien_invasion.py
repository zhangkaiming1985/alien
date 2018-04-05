import sys

import pygame

import game_functions as gf

from settings import Settings
from ship import Ship


def run_game():
	# 初始化pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
	pygame.display.set_caption(ai_settings.caption)
	ship = Ship(screen)

	# 开始游戏主循环
	while True:

		# 监视键盘和鼠标事件
		gf.check_events()
		# 更新屏幕
		gf.updata_screen(ai_settings, screen, ship)


run_game()
