import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet
from game_stats import Gamestats
from button import Button
from score import Scoreboard


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))     #设立一个像素为1200,800的显示窗口
    pygame.display.set_caption("alien_game")                     #set_mode的实参为一个元组
    ship = Ship(screen,ai_setting)                               #创建飞船
    bullets = Group()                                            #创建一个子弹元组
    #alien = Alien(screen,ai_setting)                            #创建一个外星人
    aliens = Group()                                             #创建一个外星人编组

    #用于构建一个群
    gf.create_fleet(ai_setting,screen,ship,aliens)
    
    #用于绘制按钮
    play_button = Button(ai_setting,screen,"play") 
    
    
    #用于统计游戏信息
    stats = Gamestats(ai_setting)

    #计分牌
    sb = Scoreboard(ai_setting,stats,screen)

    
    #开始 游戏主循环

    while True:

        #用于管理事件(要处在游戏启动之外)
        gf.chck_events(ai_setting,screen,ship,aliens,bullets,stats,play_button,sb)

        if stats.game_active:
            #用于移动飞船
            ship.updata()
            #用于发射子弹
            gf.updata_bullets(bullets,aliens,ai_setting,screen,ship,stats,sb)
            #用于外星人移动
            gf.update_aliens(ai_setting,screen,stats,ship,bullets,aliens,sb)
        

        #用于显示图像
        gf.update_screen(screen,ai_setting,ship,aliens,bullets,stats,play_button,sb)
       
        
run_game()
                
    
