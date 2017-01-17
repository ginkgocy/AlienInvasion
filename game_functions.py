#!/usr/bin/python
#coding:utf-8

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	stats_ships_left = 1
	aliens.empty()
	bullets.empty()
	create_fleet(ai_settings, screen, ship, aliens)
	ship.center_ship()
	sleep(0.5)
	

def check_events(ai_settings,screen,ship,bullets):
	""" 响应鼠标事件 """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			chek_keyup_events(event,ai_settings,screen, ship)
# 响应按键按下事件
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right =True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
			
# 响应按键松开事件
def chek_keyup_events(event,ai_settings,screen,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
	# 检测是否有子弹击中外星人，并删除子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True) # 后两个参数分别对应是否删除子弹和外星人
	if len(aliens) == 0:
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)
	
	
# 绘制屏幕上的内容	
def update_screen(ai_settings,screen,ship,aliens,bullets):
	""" 更新屏幕上的图像，并切换到新屏幕"""
	# 每次循环时都会重绘屏幕
	screen.fill(ai_settings.bg_color)
	for bullet in bullets:
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	# 让最近绘制的屏幕可见
	pygame.display.flip()
	
# 更新子弹
def update_bullets(ai_settings,screen,ship,aliens,bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
	
# 更新所有外星人的位置
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		print "Ship hit !!!"
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


# 生成子弹
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
		
def create_fleet(ai_settings,screen,ship,aliens):
	""" 创建外星人 """
	alien = Alien(ai_settings, screen)
	alien_number_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height , alien.rect.height)
	
	#创建第一行外星人
	for row_number in range(number_rows):
		for alien_number in range(alien_number_x):
			create_alien(ai_settings, screen, aliens, alien_number,row_number)
		
		
def get_number_aliens_x(ai_settings,alien_width):
	""" 计算屏幕能容纳多少外星人 """ 
	avaibale_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(avaibale_space_x / (2 * alien_width))
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	#创建一个外星人并将其加入当前行
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x =  alien_width + 2 * alien_width *alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
	""" 计算可以容纳多少行外星人 """	
	availabel_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
	number_rows = int(availabel_space_y / (2 * alien_height))
	return number_rows

def check_fleet_edges(ai_settings,aliens):
	""" 有外星人到达边缘时采取相应的措施 """
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	""" 将整群外星人下移，并改变他们的方向 """
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
	

		
	
	
	
	
	
	
	
	
	
	