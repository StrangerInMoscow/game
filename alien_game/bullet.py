"""bullet模块用于管理子弹"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """建设一个子弹类"""
    def __init__(self,ai_setting,screen,ship):
        """用于初始化子弹图像和基本配置"""
        super().__init__()
        self.screen  = screen

        #在0,0处创建一个子弹矩形，用于图像存储
        self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #用小数表示子弹的位置
        self.y = float(self.rect.y)

        #存储子弹颜色和速度
        self.speed_factor = ai_setting.bullet_speed_factor
        self.color = ai_setting.bullet_color
        
    


    def update(self):
        """向上移动子弹"""
        self.y -= self.speed_factor
        self.rect.y = self.y
            
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)










        
