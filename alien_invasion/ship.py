## 创建Ship类，负责管理飞船的行为。
## 选择好图片后需要将其显示到屏幕上。
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """管理飞船的类"""
    def __init__(self,ai_game):  ## 接受两个参数，一个是self，一个是指向当前AlienInvasion实例的引用。
        ## 这让Ship能够访问AlienInvasion中定义的所有游戏资源
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen  ## 将屏幕赋值给ship的一个属性，便于在这个类的所有的方法中可以访问。

        ## 给Ship类添加属性settings，以便在update()方法中可以使用这个属性。
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  ##  使用方法get_rect()访问屏幕的属性rect并将其赋值给self.screen_rect,可以将飞创放在正确的位置。
        ## rect是矩形的意思，pygame可以以处理矩形的方式处理所有的游戏元素
        ## 可以快速判断是否元素之间发生了碰撞。

        # 加载飞船图像并获取其外接矩形。
        self.image = pygame.image.load('images/ship.bmp')  ## 使用pygame.image.load()加载图像，并将其位置传递给它。
        ## 返回一个surface，然后将这个surface赋值给self.image
        self.rect = self.image.get_rect()  ## 使用get_rect()获取surface的属性赋值给rect，后面可以使用它来指定飞船的位置

        # 对于每艘新飞船，都将其放在屏幕底部的中央。
        self.rect.midbottom = self.screen_rect.midbottom
        ## 处理rect对象时，可以使用矩形四角和中心的x和y坐标，设置这些值来确定矩形的位置，也就是我们的元素的位置。
        ## 在Pygame中远点在屏幕的左上角（0,0）坐标，可以使用x和y的坐标表示，也可以使用rect对象的属性
        ## 要使游戏元素与屏幕对齐可使用属性，top、bottom、left和right
        
        ## 允许持续移动，设置一个标志，当用户没有按键盘时，标志为False，当按下为True，送开始为False。
        
        ## 在飞船的的属性X中储存小数值。
        self.x = float(self.rect.x)  ## 将self.rect.x 转换为小数并且赋值给self.x

        # 移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x值
        # 限制飞船的活动范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
       
        #if self.moving_right:
        #    self.rect.x += 1
        #if self.moving_left:
        #    self.rect.x -= 1
        
        # 根据self.x更新rect对象。
        self.rect.x = self.x
        

    def blitme(self):  ## 定义了方法，它的功能是将图像绘制在self.rect的指定的位置
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        """让飞船在屏幕低端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

## 在屏幕上绘制飞船，更新alien_invasion.py 模块。
## 允许持续移动，设置一个标志，当用户没有按键盘时，标志为False，当按下为True，送开始为False。
   
