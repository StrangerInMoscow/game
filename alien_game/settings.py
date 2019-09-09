"""settings模块，用于对游戏的各种设置"""

class Settings():
    """存储《外星人入侵》中的所有设置类"""

    def __init__(self):
        """初始化游戏静态设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.color = (230,230,230)
       
        #子弹设置
        self.bullet_height = 15
        self.bullet_color = 60,60,60

        #飞船数量
        self.ship_limt = 3
        
        #以什么样的节奏加快游戏
        self.speedup_scale = 1.3

        self.dynamic_setting()
        


    def dynamic_setting(self):
        """初始化游戏随游戏进行而变化"""
        #子弹宽度
        self.bullet_width = 3
        
        #飞船速度设置
        self.ship_speed_factor = 1.5
        
        #子弹速度设置
        self.bullet_speed_factor = 3
        
        #触碰方向设置，f_d 为1表示右移，为-1表示左移
        self.f_d = 1

        #外星人纵向和横向速度设置
        self.al_speed = 1
        self.al_dspeed = 10

        #击落外星人得分为50
        self.alien_points = 50

    def increase_speed(self):
        """随游戏进行速度变化设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.al_speed *= self.speedup_scale
        if self.bullet_width <= 100:
            self.bullet_width *= 3

        self.alien_points = int(self.alien_points * 1.5)
        
        
        











        
        
