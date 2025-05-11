import pygame
from pygame.sprite import Sprite  ## 导入sprite模块中的类Sprite，精灵

class Bullet(Sprite):
    """管理飞船所发射子弹的类"""
    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹的对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        ## 在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,  ## 因为子弹不是位图，因此使用pygame.Rect()方法创建了一个矩形
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop  ##  将飞船的rect属性赋值给了子弹的rect属性，会这样子弹和飞船就会在同一个位置。

        # 储存用小数表示的子弹位置
        self.y = float(self.rect.y)
    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
