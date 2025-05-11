## 创建一个背景为蓝色的Pygame窗口
import sys
import pygame
class BlueSky:
    def __init__(self):
        """初始化屏幕"""
        pygame.init()
        ## 创建屏幕
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Blue Sky")

        ## 设置背景颜色
        self.bg_color = (67,142,219)

    ## 主循环
    def run(self):
        """定义主循环，显示窗口"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # 填充背景颜色
            self.screen.fill(self.bg_color)
            # 更新显示
            pygame.display.flip()
if __name__ == '__main__':
    blue_sky = BlueSky() 
    blue_sky.run()

