#coding:utf-8
#!/usr/bin/python

# 环境：Python 2.7.10
# 外星人入侵学习demo

import sys
import pygame
import game_functions as gf

from alien_invasion_setting import Settings
from ship import Ship
from game_stats import GameStats
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	play_button = Button(ai_settings, screen, "Play")
	
	ship = Ship(ai_settings,screen)
	
	# 创建一个用于存储子弹的编组
	bullets = Group()
	
	# 创建用于存储外星人的编组
	aliens = Group()
	
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	while True:
		# 事件监测
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			# 飞船属性更新	
			ship.update()	
			# 更新子弹的位置信息									
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			# 更新外星人的位置							
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)	
		# 设置窗口背景颜色			
		screen.fill(ai_settings.bg_color)	
		# 更新屏幕上绘制的内容				
		gf.update_screen(ai_settings, screen,stats,sb,ship,aliens,bullets,play_button) 

run_game()