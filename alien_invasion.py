import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from game_status import GameStatus
from ship import Ship
from button import Button
from scoreboard import Scroeboard


def run_game():
	# 初始化pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)
	play_button = Button(screen, 'PLAY')

	status = GameStatus(ai_settings)
	scoreboard = Scroeboard(screen, ai_settings, status)
	ship = Ship(screen, ai_settings)
	bullets = Group()
	aliens = Group()

	# 创建外星人集群
	gf.create_fleet(screen, ai_settings, aliens, ship)

	# 开始游戏主循环
	while True:

		# 监视键盘和鼠标事件
		gf.check_events(ship, bullets, screen, ai_settings, status, play_button, aliens, scoreboard)

		if status.game_active is True:
			# 更新飞船
			ship.update()
			# 更新子弹
			gf.update_bullets(bullets, aliens, screen, ai_settings, ship, status, scoreboard)
			# 更新外星人
			gf.update_aliens(aliens, ai_settings, ship, status, bullets, screen, scoreboard)
		# 更新屏幕
		gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, status, scoreboard)


run_game()
