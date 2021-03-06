import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


def check_events(ship, bullets, screen, ai_settings, status, play_button, aliens, scoreboard):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x = pygame.mouse.get_pos()
			check_play_button(status, play_button, mouse_x, aliens, bullets, ship, screen, ai_settings, scoreboard)

		# 游戏活动状态时，检测左右按键并作出响应
		if status.game_active is True:
			if event.type == pygame.KEYDOWN:
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


def check_play_button(status, play_button, mouse_x, aliens, bullets, ship, screen, ai_settings, scoreboard):
	"""鼠标左键单击play，开始游戏"""
	button_clicked = play_button.rect.collidepoint(mouse_x)
	if button_clicked and (status.game_active is False):
		# 重置游戏信息
		ai_settings.initialize_dynamic_settings()
		status.reset_status()
		status.game_active = True

		# 游戏活动时隐藏光标
		pygame.mouse.set_visible(False)

		# 刷新得分板
		scoreboard.prep_score()
		scoreboard.prep_high_score()
		scoreboard.prep_level()
		scoreboard.prep_ship()

		# 清空外星人和子弹，飞船居中
		aliens.empty()
		bullets.empty()
		ship.center_ship()

		# 创建一群外星人
		create_fleet(screen, ai_settings, aliens, ship)


def update_bullets(bullets, aliens, screen, ai_settings, ship, status, scoreboard):
	"""更新子弹位置并去除消失的子弹"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)
	check_bullet_alien_collections(screen, ai_settings, aliens, ship, bullets, status, scoreboard)


def check_bullet_alien_collections(screen, ai_settings, aliens, ship, bullets, status, scoreboard):
	"""检测子弹与外星人碰撞"""

	# 检查是否有子弹击中外星人，若有则删除相应子弹和外星人
	collections = pygame.sprite.groupcollide(bullets, aliens, True, True)
	# 若发生碰撞，则增加得分
	if collections:
		for a in collections.values():  # 在collection中，碰撞的子弹是一个键，所有与每颗子弹相关的值都是列表，包含该子弹碰撞的外星人
			status.score += ai_settings.alien_points * len(a)
			scoreboard.prep_score()
		check_high_score(status, scoreboard)
	# 若外星人群全部被消灭，则新建一组，并提高游戏难度
	if len(aliens) == 0:
		bullets.empty()
		ai_settings.increase_speed()
		# 更新等级
		status.level += 1
		scoreboard.prep_level()

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


def update_aliens(aliens, ai_settings, ship, status, bullets, screen, scoreboard):
	"""更新外星人位置"""
	# 检查外星人群是否到达边缘
	check_fleet_edges(aliens, ai_settings)
	aliens.update()

	# 检查外星人与飞船是否发生碰撞，若是则执行ship_hit()
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(status, aliens, bullets, screen, ai_settings, ship, scoreboard)
	# 检查外星人是否到达屏幕底端，若是则执行ship_hit()
	for alien in aliens:
		if alien.check_bottom():
			ship_hit(status, aliens, bullets, screen, ai_settings, ship, scoreboard)
			break


def ship_hit(status, aliens, bullets, screen, ai_settings, ship, scoreboard):
	"""飞船被击中"""
	if status.ship_left > 0:
		# 飞船-1
		status.ship_left -= 1
		scoreboard.prep_ship()
		# 重置外星人、子弹、飞船位置
		aliens.empty()
		bullets.empty()
		create_fleet(screen, ai_settings, aliens, ship)
		ship.center_ship()
		# 暂停
		sleep(1)
	else:
		status.game_active = False
		# 显示光标
		pygame.mouse.set_visible(True)


def check_high_score(status, scoreboard):
	"""检查是否产生新的最高分"""
	if status.high_score < status.score:
		status.high_score = status.score
		scoreboard.prep_high_score()


def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, status, scoreboard):
	"""更新屏幕图像， 切换到新屏幕"""

	# 每次循环重新绘制屏幕
	screen.fill(ai_settings.bg_color)
	# 绘制记分板
	scoreboard.draw_score()
	# 绘制飞船
	ship.blitme()
	# 绘制外星人
	aliens.draw(screen)
	# 绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	if (status.game_active is False):
		play_button.draw_button()

	# 让最近绘制的屏幕可见
	pygame.display.flip()
