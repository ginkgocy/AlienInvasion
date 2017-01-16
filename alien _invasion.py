#coding:utf-8
#!/usr/bin/python

# 环境：Python 2.7.10
# 外星人入侵学习demo

import sys
import pygame

from alien_invasion_setting import Settings
from ship import Ship
from pygame.sprite import Group

import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	ship = Ship(ai_settings,screen)
	
	# 创建一个用于存储子弹的编组
	bullets = Group()
	
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)	#事件监测
		ship.update()										#飞船属性更新
		gf.update_bullets(bullets)							#更新子弹的位置信息
		screen.fill(ai_settings.bg_color)					#设置窗口背景颜色
		gf.update_screen(ai_settings, screen, ship,bullets) #更新屏幕上绘制的内容
		
run_game()