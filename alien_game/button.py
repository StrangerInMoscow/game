"""此模块用于创建带标签的实心矩形充当按钮来控制游戏"""

import pygame.font

class Button():
    """用于添加按钮的类"""
    def __init__(self,ai_setting,screen,msg):
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮的尺寸及其他属性
        self.width, self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)

        #指定用什么字体来渲染，并指定字号
        self.font = pygame.font.SysFont(None,48)

        #创建按钮并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将要输入的文本渲染为图像并添加在按钮上"""
        #参数分别为，要渲染的文本，是否开启抗锯齿，文本颜色，背景颜色
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        """绘制一个用颜色填充的按钮，在绘制文本"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        

        








        
    
