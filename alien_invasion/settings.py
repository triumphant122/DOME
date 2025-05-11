## 创建设置类
## 编写一个名为setting的模块，其中包含了一个名为Setting的类
## 作用是储存所有设置的地方，可以避免在代码中到处设置选项，要修改游戏只需要修改settings.py中的值，不需要在主程序当中找到在修改。
class Settings:
    """储存游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置。"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船设置
        #self.ship_speed = 1.0  ## 将飞船的初始速度设置为1.5，这样，每次循环将不在移动一个像素而是1.5个像素的距离。
        self.ship_limit = 3

        # 子弹设置
        #self.bullet_speed = 1.5
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3  ## 限制子弹的个数。

        # 外星人设置
        #self.alien_speed = 0.1
        self.fleet_drop_speed = 1 ## 表示外星人移动方向的设置
        # fleet_direction为1表示向右移动，为-1表示向左移动
        #self.fleet_direction = 1

        # 加快游戏节奏
        self.speedup_scale = 1.1  # 控制游戏节奏的加快速度
        # 外星人分数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的量"""
        self.ship_speed = 0.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.1
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50
    def increase_speed(self):
        """提高速度设置和外星人分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
    
   
        
