"""game_functions模块用于存储游戏函数"""

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event,ai_setting,screen,ship,bullets):
    """当按键按下时"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
                
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        #创建一个子弹添加到元组中
        new_bullet = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullet)

    elif event.key == pygame.K_q:
        sys.exit()
        


def check_keyup_events(event,ship):
    """当按键抬起时"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False

    elif event.key == pygame.K_DOWN:
        ship.moving_down = False




def chck_events(ai_setting,screen,ship,aliens,bullets,stats,play_button,sb):
    """用于管理事件"""
    #创建一个 键盘和鼠标的事件循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting,screen,ship,bullets,aliens,stats,play_button,mouse_x,mouse_y,sb)


        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_setting,screen,ship,bullets)
            
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def check_play_button(ai_setting,screen,ship,bullets,aliens,stats,play_button,mouse_x,mouse_y,sb):
    """点击play按钮时开始游戏"""
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        #光标消失
        pygame.mouse.set_visible(False)
        
        #重置游戏基本速度设置
        ai_setting.dynamic_setting()

        #重置游戏统计信息
        stats.game_active = True
        stats.reset_stats()
        #stats.load_high_score()

        #重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        #清空外星人列表和子弹列表
        bullets.empty()
        aliens.empty()

        #创建一群新的外星人
        create_fleet(ai_setting,screen,ship,aliens)
        ship.center_ship()
        

def update_screen(screen,ai_setting,ship,aliens,bullets,stats,play_button,sb):
    """用于管理屏幕图像出现，并刷新屏幕"""
    #用背景颜色填充屏幕，每次循环都会重绘
    screen.fill(ai_setting.color)
    #绘制子弹
    for bullet in bullets.sprites():                         #将元组返回一个子弹列表
        bullet.draw_bullet()
    #绘制飞船
    ship.blitmes()
    
    #绘制编组里的每一个外星人
    aliens.draw(screen)
    
    #绘制得分
    sb.show_score()
    
    #游戏处于非运行状态绘制游戏开始按钮
    if not stats.game_active:
        play_button.draw_button()

    #显示屏幕(这里每进行一次循环，屏幕都会刷新一次)
    pygame.display.flip()
    

def updata_bullets(bullets,aliens,ai_setting,screen,ship,stats,sb):
    """用于发射子弹"""
     
    bullets.update()

    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien(bullets,aliens,ai_setting,screen,ship,stats,sb)
    

def check_bullet_alien(bullets,aliens,ai_setting,screen,ship,stats,sb):
    """碰撞检测"""

    #碰撞检测删除已消失的机器人和子弹(返回的是一个字典)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    #检测是否击落外星人，击落外星人，分值加1,并重新渲染图像
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_setting.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    
    #看外星人是否为空，要为空，删除子弹，重新造一批更快的外星人
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()

        #提高等级
        stats.level += 1
        sb.prep_level()

        #新建一批外星人
        create_fleet(ai_setting,screen,ship,aliens)
        

def get_number_aliens_x(ai_setting,alien_width):
    """计算每行可容纳多少外星人"""
    #计算外星人所需的水平空间，可容纳多少外星人
    al_x = ai_setting.screen_width - 2 * alien_width
    number_x = int(al_x / (2 * alien_width))
    return number_x


def get_number_rows(ai_setting,ship_height,alien_height):
    """计算屏幕可以容纳多少行外星人"""
    al_y = (ai_setting.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(al_y / (2 * alien_height))
    return number_rows


def creat_alien(ai_setting,screen,aliens,al_number,row_number):
    """创建一个外星人并放在当前行"""
    #计算一群外星人所占空间，并创建一个外星人并放在当前行，
    alien = Alien(screen,ai_setting)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * al_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
   

   
def create_fleet(ai_setting,screen,ship,aliens):
    """构建外星群"""
    #先构建一个外星人，再看一行可容纳多少外星人
    alien = Alien(screen,ai_setting)
    number_x = get_number_aliens_x(ai_setting,alien.rect.width)
    #看外星人能容纳多少行
    number_rows = get_number_rows(ai_setting,ship.rect.height,alien.rect.height)

    #创建外星人群
    for row_number in range(number_rows):
        for al_number in range(number_x):
            creat_alien(ai_setting,screen,aliens,al_number,row_number)


def chck_f_e(ai_setting,aliens):
    """有外星人到达边缘时采取措施"""
    #只有其中一个碰到便改变方向，不影响全部
    for alien in aliens.sprites():
        if alien.check_e():
            change_f_d(ai_setting,aliens)
            break
        


def change_f_d(ai_setting,aliens):
    """将整群外星人下移并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.al_dspeed
    ai_setting.f_d *= -1


def ship_hit(ai_setting,screen,stats,ship,bullets,aliens,sb):
    """处理外星人碰到飞船"""
    #将飞船数量减1
    stats.ship_left -= 1
    sb.prep_ships()

    #判断游戏是否进行
    if stats.ship_left > 0:

        #清空外星人列表和子弹列表
        bullets.empty()
        aliens.empty()

        #创建一批新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_setting,screen,ship,aliens)
        ship.center_ship()

        #暂停
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def chck_a_b(ai_setting,screen,stats,ship,bullets,aliens,sb):
    """检查外星人碰到底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
             #如果外星人撞到底端就像飞船被撞到那样处理
            ship_hit(ai_setting,screen,stats,ship,bullets,aliens,sb)
            break
    
    
def update_aliens(ai_setting,screen,stats,ship,bullets,aliens,sb):
    """外星人移动并检测碰撞后移动"""
    chck_f_e(ai_setting,aliens)
    aliens.update()

    #检测外星人和飞船间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_setting,screen,stats,ship,bullets,aliens,sb)

    #检测外星人与飞船间的碰撞
    chck_a_b(ai_setting,screen,stats,ship,bullets,aliens,sb)   
    
       
def check_high_score(stats,sb):
    """检查是否是最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
        stats.dump_high_score()













