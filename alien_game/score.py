"""此模块用于记录分数"""
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """显示得分信息的类"""
    def __init__(self,ai_setting,stats,screen):
        """初始化显示得分所设立的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats

        #显示得分信息时所用的字体设计
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #准备初始得分和最高得分包括等级图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        """将得分渲染为一副图像"""
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,
            self.ai_setting.color)
        
        #将图像放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高得分渲染为一张图像"""
        high_score = int(round(self.stats.high_score,-1))
        high_score = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score,True,self.text_color,
            self.ai_setting.color)

        #将最高得分放在屏幕正上方
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """将等级渲染为一张图像"""
        level = str(self.stats.level)
        self.level_image = self.font.render(level,True,self.text_color,self.ai_setting.color)

        #将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示余下多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.screen,self.ai_setting)
            ship.rect.x = 10 + ship.rect.width * ship_number
            ship.rect.y = 10
            self.ships.add(ship)
        

    def show_score(self):
        """在屏幕上显示得分和最高得分和等级"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        #绘制飞船，知道还剩多少
        self.ships.draw(self.screen)

    
        
















