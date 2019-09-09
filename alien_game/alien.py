"""aline模块用于添加外星人"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """单个外星人类"""
    def __init__(self,screen,ai_setting):
        """初始化外星人属性及图像"""
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        #加载外星人图像
        self.image = pygame.image.load(r'images\alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #让外星人出现在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitem(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)


    def check_e(self):
        """外星人处于屏幕边缘就返回TRUE"""
        if self.rect.right >= self.screen_rect.right:
            return True

        elif self.rect.left <= 0:
            return True


    def update(self):
        """向右移动外星人"""
        self.x += (self.ai_setting.al_speed * self.ai_setting.f_d)
        self.rect.x = self.x

    
    
        
        
    







        
