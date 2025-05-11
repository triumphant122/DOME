from random import choice  ## 使用choice来选择使用哪种
class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points=5000):  ## 将随机漫步包含的默认点数设置为5000
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]
    
    def get_step(self):
        """生成一个方向的步长（方向+距离）"""
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        return direction * distance

    ## 重构fill_walk类，使用get_step方法进行简化
    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步直到达到了指定的点数
        while len(self.x_values) < self.num_points:
            # 通过get_step()获取x和y方向和步长
            x_step = self.get_step()
            y_step = self.get_step()



            # 决定前进方向以及沿这个方向前进的距离。
            #x_direction = choice([1,-1])  ## 决定向左还是向右，choice函数选择-1和1，-1向左，1向右

            #x_distance = choice([0,1,2,3,4]) ## 决定走多远
            #x_step = x_distance * x_direction

            #y_direction = choice([1,-1])
            #y_distance = choice([0,1,2,3,4])
            #y_step = y_distance * y_direction

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值。
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

## 重构思路
## 原来是将x和y的方向分别创建并且进行储存，重构后使用方法get_step()不需要分开。
## 直接方向储存一次，步数储存一次，然后将这个方法返回一个步数乘方向。
## 在后续调用时在分成x轴方向和y轴方向减少了工作量