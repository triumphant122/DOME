## 创建Pygame窗口及响应用户输入
import sys  ## 导入sys模块用来退出游戏
from time import sleep ## 导入time模块，在飞船撞到外星人之后让游戏暂停片刻

import pygame  ## 导入pygame模块，它包含了开发游戏所需的功能
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship ## 导入Ship类
from bullet import Bullet
from alien import Alien  ## 导入Alien类



class AlienInvasion:  ## 创建了一个类，来管理游戏资源和游戏中的行为，这个类表示这个游戏。
    """管理游戏资源和行为的类"""
    def __init__(self):  ## __init__初始化游戏
        """初始化游戏并且创建游戏资源"""
        pygame.init()  ## 初始化背景设置。
        self.settings = Settings()  ## 在主程序文件当中导入了Settings类,创建了一个实例并将其赋值给self.settings。
        ## 后续在创建屏幕、填充背景颜色时使用了self.settings的属性
        ## self.screen = pygame.display.set_mode((1200,800))  ## 使用了pygame.display.set_mode()创建了一个窗口。
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))  ## 创建了Settings类后可直接应用其中的设置，因此将原来的代码进行了修改，引用设置类。
        
        ## pygame.display.set_mode()的实参是一个元组，规定了屏幕的大小，是元组不允许修改，具体含义是宽1200个像素，高800个像素。
        ## 创建完窗口后，将其赋值给属性self.screen,以便后面可以直接使用它。
        ## 赋给属性self.screen的对象是一个surface， 是屏幕的一部分，用于显示游戏元素，在游戏中每个元素都是一个surface，例如外星人或飞船。
        pygame.display.set_caption("Alien Invasion")  ## 给屏幕一个标题？


        # 创建一个用于储存游戏统计信息的实例
        # 并创建记分牌
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        


        self.ship = Ship(self)  ## 创建屏幕之后，创建了一个飞船的实例。调用Ship这个类时必须提供一个参数，就是AlienInvasion的实例
        ## self指向的就是当前AlienInvasion的实例，这个参数可以是ship使用游戏的资源

        # 设置背景颜色
        # self.bg_color = (230,230,230)  设置当中定义了背景颜色，因此这里也不需要进行在定义
        ## pygame中颜色由RBG值定义，(R,B,G)每个取值范围在0~255之间。
        
        ## 创建一个编组group用来储存所有有用的子弹
        self.bullets = pygame.sprite.Group()  ## 创建储存用的编组

        self.aliens = pygame.sprite.Group() ## 创建一个用来储存外星人的编组
        self._create_fleet()

        # 创建play按键
        self.play_button = Button(self,"Play")


    ## 创建外星人实例
    ## 对_creat_fleet(self): 进行重构
    def _create_fleet(self):
            """创建外星人群"""
            # 创检一个外星人并计算一行可以容纳多少个外星人
            # 外星人的间距为外星人的宽度
            alien = Alien(self)
            alien_width,alien_height  = alien.rect.size
            available_space_x = self.settings.screen_width - (2 * alien_width)
            number_alien_x = available_space_x // (2 * alien_width)

            # 计算屏幕可容纳多少行外星人
            ship_height = self.ship.rect.height
            available_space_y = (self.settings.screen_height - 
                                 (3 * alien_height) - ship_height)
            number_rows = available_space_y // (2 * alien_width)

            # 创建外星人群
            for row_number in range(number_rows):
                for alien_number in range(number_alien_x):
                    self._create_alien(alien_number,row_number) ## 从这里开始书写的较为混乱注意！！！！！
                ## self._create_alien(alien_number)  ## 书里没写这里，先注释掉，这个是最开始创建第一行外星人的for循环改写成这样
    def _create_alien(self,alien_number,row_number):
                """创建个外星人并将其加入当前行"""
                alien  = Alien(self)
                alien_width,alien_height = alien.rect.size
                alien.x = alien_width + 2 * alien_width * alien_number
                alien.rect.x = alien.x
                alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
                self.aliens.add(alien)  

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """将整群外星人下移，并改变他们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



        #"""创建外星人群"""
        # 外星人的间距为外星人的宽度
        # 创建一个外星人并计算一行可容纳多少个外星人
        #alien = Alien(self)  ## 创建了一个实例，并将其储存到外星人编组当中
        #alien_width,alien_height = alien.rect.size   ## 将外星人rect的宽度赋值给外星人的宽度
        #available_space_x = self.settings.screen_width - (2 * alien_width)  ## 计算外星人的空间，以及可以容纳多少外星人。
        #number_aliens_x = available_space_x // (2 * alien_width)


         # 计算屏幕可以容纳多少行外星人
      #  ship_height = self.ship.rect.height
       # available_space_y = (self.settings.screen_height - 
        #                     (3 * alien_height) - ship_height)
        #number_rows = available_space_y // (2 * alien_height)
        # 创建外星人群
       # for row_number in range(number_rows):
            #for alien_number in range(number_aliens_x):
               # self._create_alien(alien_number,row_number)

        # 创建第一行外星人
        #for alien_number in range(number_aliens_x):
           # self._create_alien(alien_number)
    #def _create_alien(self,alien_number,row_number):
     #   """创建一个外星人并将其加入到当前行"""
      #  alien = Alien(self)
       # alien_width,alien_height = alien.rect.size
        #alien.x = alien_width + 2 * alien_width * alien_number
        #alien.rect.x = alien.x
        #alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        #self.aliens.add(alien)
          

         

         
    # 创建第一行外星人。
        #for alien_number in range(number_aliens_x):
            #self._create_alien(alien_number)
            # 创建一个外星人并将其加入到当前行
           # alien = Alien(self)
            #alien.x = alien_width + 2 * alien_width * alien_number
           # alien.rect.x = alien.x
           # self.aliens.add(alien)
    

    def run_game(self):  ## 控制游戏的启动，其中包含了一个while循环。
        """开始游戏的主循环"""
        while True:
            self._check_events()
            ## 将原先监视键盘和鼠标事件的代码定义为一个方法，并将原来的代码全部移入定义的方法中，这里直接调用这个响应时间的方法。
            if self.stats.game_active:

                self.ship.update()
            ## 每次循环都调用飞船模块的update方法进行移动飞船

            ## 将更新子弹位置的代码写到while循环当中。
            ##self.bullets.update()
            ## 删除消失的子弹，子弹飞出屏幕外之后并没有消失而还在消耗电脑资源
           # for bullet in self.bullets.copy():  ## 在编组中遍历子弹。
                ## python要求该列表的长度保持不变，因此不能在遍历当中直接删除，所以这里遍历的时编组的副本，使用方法copy()来完成，从而在循环中修改编组。
               # if bullet.rect.bottom <= 0:  ## 当子弹的rect属性是否小于0，如果是的话就从编组中将它删除。
                    #self.bullets.remove(bullet)
           # print(len(self.bullets))  ## 打印编组中还剩多少子弹，也就是屏幕中包括飞出屏幕的子弹有多少。
            ## 将上述大代码单独编写一个方法，使主程序文件看起来更简洁
                self._update_bullets()

            ## 调用更新每个外星人位置的方法
                self._update_aliens()


            self._update_screen()
            ## 将原先绘制屏幕的代码定义一个新方法，并且将原来的代码移到新方法当中，在这里调用这个方法
           
            # 监视键盘和鼠标事件。
            #for event in pygame.event.get():  ## 事件循环，事件是用户在玩游戏时执行的操作，鼠标移动，键盘输入。
                ## 使用pygame.event.get()来访问Pygame检测到的事件。
                ## 返回值是一个列表，其中包含了上次被调用之后发生的所有事情，所有的鼠标和键盘事件都会导致这个for循环运行。
            #    if event.type == pygame.QUIT:  ## 编写了if语句来检测特定事件。当玩家用鼠标点击关闭时将调用sys.exit()退出游戏。
            #        sys.exit()
            
            # 每次循环都重绘屏幕
            # self.screen.fill(self.bg_color)  ## 调用fill()函数填充屏幕
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()  ## 调用这个函数，使在指定的位置绘制飞船
            # 让最近绘制的屏幕可见
            # pygame.display.flip()  ## 每次执行while循环都会绘制一个新屏幕，并且替换旧屏幕，用来更新元素的位置。
    

            
          
    ## 对_check_events(self):进行重构，将其中的代码放在两个方法中一个响应KEYDOWN 一个响应KEYUP
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            ## 在模块ship中定义了移动标志，因此要在此处对最初的代码进行修改,以便在检测到键盘输入后将标志改为True进行移动。
            ## 因为ship模块添加了向左移动的标志，因此此处代码也需要进行修改

            elif event.type == pygame.KEYDOWN:
                 self._check_keydown_events(event)
                #if event.key == pygame.K_RIGHT:
                    #self.ship.moving_right = True
                #elif event.key == pygame.K_LEFT:
                    #self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                #if event.key == pygame.K_RIGHT:
                   # self.ship.moving_right = False
               # elif event.key == pygame.K_LEFT:
                 #   self.ship.moving_left = False
            ## 将原来的代码修改为，不直接调整飞船的位置而是将移动的标志改为True和Fasle.
            ## 检测用户鼠标点击了按钮
            elif event.type == pygame.MOUSEBUTTONDOWN: # 论用户点击屏幕什么位置都会检测到一个事件发生
                mouse_pos = pygame.mouse.get_pos()  ## 返回一个元组，其中记录了用户点击位置的X和Y值。
                self._check_play_button(mouse_pos)   ## 将上述的值传递给这个方法。
            
            #elif event.type == pygame.KEYDOWN:  ## 添加了一个elif分支，在检测到KEYDOWN时做出反应，猜测应该是检测到键盘敲击。
            #    if event.ket == pygame.K_RIGHT:  ## 检测按下的建是不是又建，如果是的话，飞船的矩阵rect的x坐标加1，也就是x坐标向右移动一个点。
                    # 向右移动飞船。
            #        self.ship.rect.x += 1
    def _check_play_button(self,mouse_pos):
         """在玩家点击Play按钮时，开始游戏"""
         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
         if button_clicked and not self.stats.game_active:
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()
            # 重置游戏得分
            self.sb.prep_score()
            # 重置游戏等级
            self.sb.prep_level()
            # 重置剩余飞船
            self.sb.prep_ships()

            # 隐藏鼠标光标
            pygame.mouse.set_visible(False)  ## 没有效果，先不管
            # print(pygame.mouse.get_visible())

            # 重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人并让飞船居中
            self._create_fleet()
            self.ship.center_ship()

            

    ## 创建了两个新的辅助方法，将原来的_check_events()进行重构，将原来一个代码重构成两个辅助方法，使代码 看起来更简洁
    def _check_keydown_events(self,event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        ## 在按键响应的分支中添加一个q快捷退出按键
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:  ## 添加一个elif分支按下空格键触发下面辅助方法
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """更新子弹的位置，并且删除超出屏幕的子弹"""
        # 更新子弹的位置
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        #print(len(self.bullets))

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞"""
        # 检查是否有子弹击中了外星人
        # 如果是，就删除响应的外星人和子弹
        # 删除发生碰撞的外星人和子弹
        collisions = pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True)  ## 将子弹编组和外星人编组当中的元素的rect属性进行对比，当rect重叠时，就会在返回的字典中添加一个键值对。
        ## sprite.groupcollide()会创建一个字典，其中两个编组中的rect值一个是键一个是对应的值。
        ## 两个实参True让pygame删除碰撞的两个元素，当第一个改为False时，可以不删除子弹，只删除外星人，子弹会执行之前的代码，碰到屏幕后消失。
        
        # 更新得分
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens) ## 
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:  ## 检查编组是否为空
            # 删除现有的子弹并新建一群外星人
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 提高等级
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """响应飞船被外星人撞到"""
        if self.stats.ships_left > 0:
            # 将ships_left减1并更新记分牌
            self.stats.ships_left -= 1
            self.sb.prep_ships()

             # 清空余下的外星人外星人和子弹。
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人，并将飞船放到屏幕低端中央。
            self._create_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)  
        
    # 管理外星人移动的方法
    def _update_aliens(self):
        """
        检查是否有外星人位于屏幕边缘，
        并更新整群外星人的位置
        """
        self._check_fleet_edges()
        self.aliens.update()  ## 对整个aliens编组调用update方法。

        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):  ## 此处接受两个实参，一个精灵和一个编组
            self._ship_hit()
            #print("Ship hit!!!")
        # 检查是否有外星人到达了屏幕底端
        self._check_aliens_bottom()

                
    #创建发射子弹的辅助方法
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        ## 将新设置的子弹个数编写到该代码当中
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)  ## 创建一个实例并将其赋值给new_bullet，在使用add将其加入到编组当中。
            self.bullets.add(new_bullet)  ## add()方法，类似于append()

    def _update_screen(self):
        """更新屏幕上图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

            ## 需要对外星人编组调用draw()方法，绘制外星人
        self.aliens.draw(self.screen)  ## 将编组中每个元素绘制到rect属性的指定位置
        # 显示得分
        self.sb.show_score()
        
        # 如果游戏处于非活跃状态，就绘制Play按钮。
        if not self.stats.game_active:  ## 如果这个值不是True 就会执行下面代码，创建按钮，实际上我们设置的是False。
            self.play_button.draw_button()
        pygame.display.flip()

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理
                self._ship_hit()
                break
if __name__ == '__main__':  ## 仅当直接直接执行时才会执行该代码
    ai = AlienInvasion()  
    ai.run_game()  ## 创建了一个实例并且调用了run_game()函数

## 绘制玩家的飞船，加载一个图片并且使用pygame的blit()绘制它。
## 可以使用任何类型的图像文件，但是使用位图（.bmp）文件最简单
## 使用其他类型图像文件，要求安装相应的图像库。
## 大多数为.jpg、.png或.gif格式，可以使用相应的软件转换为位图。

## 重构_check_events()和__update_screen()简化既有代码的结构，使其更容易扩展
## 辅助方法，在类中执行任务，但不是通过实例调用的，赋值方法的命名以单个下划线开头

## 为了进一步简化run_game()我们将更新屏幕的代码移到一个名为_update_screen()的代码当中

## 响应按键，通俗就是能够通过键盘方向键控制飞船移动。
## 使用相同的逻辑对向左移动也进行修改

## 这里有一个点，在ship模块中修改移动时使用了if，而在本模块中修改标志状态时使用了elif语句
## 因为在移动时如果使用elif后，if会处于优先状态，会使移动位置不准确，会优先向右移动。
## 而本模块中使用elif是因为每个事件都只与一个键相关联，同时按下会触发两个事件
## 没太看懂。。。。。。。。。。。。。。。。。。。。。。之前那个按下左右都只触发同一个事件，就是让飞船位置变化？？？？？

## 接下来优化飞船的速度，限制飞船的移动距离，以免消失在屏幕之外
## 在settings模块进行修改。