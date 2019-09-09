"""ship模块管理飞船"""
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船"""
    
    def __init__(self,screen,ai_setting):
        """初始化飞船以及他的位置"""
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        #加载飞船并获取其外接矩形
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()                   #让飞船获取矩形属性从而好调整位置
        self.screen_rect = self.screen.get_rect()           #让获取屏幕的矩形是飞船相互调整
        

        #将每艘飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx        #将屏幕矩形属性的具体位置给飞船，实现飞船的位置
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性中ceneter中，存储小数值。
        self.center = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)
        
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    #绘制图像的函数    
    def blitmes(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def updata(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center2 -= self.ai_setting.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center2 += self.ai_setting.ship_speed_factor

        

        #根据self.center的值更新rect对象
        self.rect.centerx = self.center
        self.rect.centery = self.center2


    def center_ship(self):
        """发生碰撞之后飞船出现在屏幕底端中央"""
        self.center = self.screen_rect.centerx
        self.center2 = self.screen_rect.bottom - self.rect.width / 2
        
    
    










    
