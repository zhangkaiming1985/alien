import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from bullet import Bullet


def run_game():
	# 初始化pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
	pygame.display.set_caption(ai_settings.caption)
	ship = Ship(screen, ai_settings)
	bullets = Group()

	# 开始游戏主循环
	while True:

		# 监视键盘和鼠标事件
		gf.check_events(ship, bullets, screen, ai_settings)
		# 更新飞船
		ship.update()
		# 更新子弹
		gf.update_bullets(bullets)
		# 更新屏幕
		gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
