#coding:utf-8
#!/usr/bin/python
# 游戏设置属性
class Settings(object):
	""" 存储《外星人入侵》的所有设置的类 """
	def __init__(self):
		# 窗口属性
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		# 飞船属性
		self.ship_speed_factor = 4
		
		# 子弹属性
		self.bullets_allowed = 10
		self.bullet_speed_factor = 5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		
		# 外星人属性
		self.alien_speed_factor = 2
		self.fleet_drop_speed = 10
		
		# fleet_direction 1 表示向右移动，为-1表示向左移动
		self.fleet_direction = 1
		self.ship_limit = 3