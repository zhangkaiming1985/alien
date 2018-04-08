import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien

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
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_event(event, ship):
	# 抬起按键
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_bullets(bullets, aliens, screen, ai_settings, ship):
	"""更新子弹位置并去除消失的子弹"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)
	check_bullet_alien_collections(screen, ai_settings, aliens, ship, bullets)


def	check_bullet_alien_collections(screen, ai_settings, aliens, ship, bullets):
	"""检测子弹与外星人碰撞"""

	# 检查是否有子弹击中外星人，若有则删除相应子弹和外星人
	collections = pygame.sprite.groupcollide(bullets, aliens, True, True)

	# 若外星人群全部被消灭，则新建一组
	if len(aliens) == 0:
		bullets.empty()
		create_fleet(screen, ai_settings, aliens, ship)


def fire_bullet(bullets, screen, ai_settings, ship):
	"""若未达到最大限制则发射子弹"""
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(screen, ai_settings, ship)
		bullets.add(new_bullet)


def create_fleet(screen, ai_settings, aliens, ship):
	"""创建外星人群"""
	# 创建一个外星人，计算一行可容纳多少，间距为外星人宽度
	alien = Alien(screen, ai_settings)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_aliens_y = get_number_aliens_y(ai_settings, alien.rect.height, ship.rect.height)
	# 创建第一行外星人
	for y in range(number_aliens_y):
		for x in range(number_aliens_x):
			create_alien(screen, ai_settings, aliens, x, y)


def get_number_aliens_x(ai_settings, alien_width):
	"""计算每行可容纳外星人的数量"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = available_space_x / (2 * alien_width)

	return int(number_aliens_x)


def get_number_aliens_y(ai_settings, alien_height, ship_height):
	"""计算可容纳外星人的行数"""
	available_space_y = ai_settings.screen_height - ship_height - 3 * alien_height
	number_aliens_y = available_space_y / (2 * alien_height)

	return int(number_aliens_y)


def create_alien(screen, ai_settings, aliens, number_alien_x, number_alien_y):
	"""创建一个外星人，并添加到外星人群中"""
	alien = Alien(screen, ai_settings)
	alien_width = alien.rect.width
	alien_height = alien.rect.height

	# 设置外星人坐标轴位置
	alien.rect.x = alien_width + number_alien_x * 2 * alien_width
	alien.rect.y = alien_height + number_alien_y * 2 * alien_height

	aliens.add(alien)


def check_fleet_edges(aliens, ai_settings):
	"""若外星人群到达屏幕边缘，则启动相应函数变向"""
	for alien in aliens:
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break


def change_fleet_direction(ai_settings, aliens):
	"""改变外星人群移动方向，并下沉一定距离"""
	ai_settings.fleet_direction *= -1
	for alien in aliens:
		alien.y = float(alien.rect.y)
		alien.y += ai_settings.fleet_drop_speed
		alien.rect.y = alien.y


def update_aliens(aliens, aisettings, ship, status, bullets, screen):
	"""更新外星人位置"""
	# 检查外星人群是否到达边缘
	check_fleet_edges(aliens,aisettings)
	aliens.update()

	# 检查外星人与飞船是否发生碰撞，若发生则执行ship_hit()
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(status, aliens, bullets, screen, aisettings, ship)

def ship_hit(status, aliens, bullets, screen, ai_settings, ship):
	"""飞船被击中"""
	# 飞船-1
	status.ship_left -= 1

	# 重置外星人、子弹、飞船位置
	aliens.empty()
	bullets.empty()
	create_fleet(screen, ai_settings, aliens, ship)
	ship.center_ship()

	# 暂停
	sleep(1)


def update_screen(ai_settings, screen, ship, bullets, aliens):
	"""更新屏幕图像， 切换到新屏幕"""
	# 每次循环重新绘制屏幕
	screen.fill(ai_settings.bg_color)
	# 绘制飞船
	ship.blitme()
	# 绘制外星人
	aliens.draw(screen)
	# 绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	# 让最近绘制的屏幕可见
	pygame.display.flip()
