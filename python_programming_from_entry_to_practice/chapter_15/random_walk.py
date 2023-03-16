from random import choice

class RandomWalk:
    """
    一个生成随机漫步数据的类
    随机漫步：每次行走得到的路径，每次行走都是完全随机的、没有明确放的方向
    """
    def __init__(self, num_points=5000) -> None:
        """初始化随机漫步的属性"""
        self.num_points = num_points # 存储随机漫步次数的变量
        # 所有随机漫步都始于(0, 0)
        self.x_values = [0] # 存储随机漫步经过的每个x坐标
        self.y_values = [0] # 存储随机漫步经过的每个y坐标
    
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步，直到列表达到指定长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离

            # 方向，-1：向左，1:向右
            x_direction = choice([1, -1])
            y_direction = choice([1, -1])
            
            # 距离
            x_distance = choice([0, 1, 2, 3, 4])
            y_distance = choice([0, 1, 2, 3, 4])
            
            # 移动方向乘移动距离，确定沿x轴和y轴移动的距离
            x_step = x_direction * x_distance # 为正向右移动，为负向左移动
            y_step = y_direction * y_distance # 为正向上移动，为负向下移动

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)