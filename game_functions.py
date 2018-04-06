import sys
import pygame
from bullet import Bullet

def check_events(ship, bullets, screen, ai_settings):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		# 检测左右按键并作出响应
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event, ship, bullets, screen, ai_settings)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, ship)

def check_keydown_event(event, ship, bullets, screen, ai_settings):
	# 按下按键
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(bullets, screen, ai_settings, ship)

def check_keyup_event(event, ship):
	# 抬起按键
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_bullets(bullets):
	"""更新子弹位置并去除消失的子弹"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)

def fire_bullet(bullets, screen, ai_settings, ship):
	"""若未达到最大限制则发射子弹"""
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(screen, ai_settings, ship)
		bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, bullets):
	"""更新屏幕图像， 切换到新屏幕"""
	# 每次循环重新绘制屏幕
	screen.fill(ai_settings.bg_color)
	# 绘制飞船
	ship.blitme()
	# 绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	# 让最近绘制的屏幕可见
	pygame.display.flip()
