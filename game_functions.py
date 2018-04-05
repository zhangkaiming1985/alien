import sys

import pygame


def check_events():
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


def updata_screen(ai_settings, screen, ship):
	"""更新屏幕图像， 切换到新屏幕"""
	# 每次循环重新绘制屏幕
	screen.fill(ai_settings.bg_color)
	# 绘制飞船
	ship.blitme()

	# 让最近绘制的屏幕可见
	pygame.display.flip()
