import numpy as np

def single_walk(start_pos, grid_size=50):
    """
    任务 C：单次随机游走
    返回粒子撞击边界时的电势值
    """
    x, y = start_pos
    # TODO: 编写 while 循环实现随机游走
    # TODO: 判断边界并返回对应电势 (Top: 100, others: 0)
    return 0.0

def solve_laplace_at_point(start_pos, n_particles=5000):
    """
    利用大量粒子游走估计某一点的电势
    """
    # TODO: 循环释放粒子并求平均电势
    return 0.0

if __name__ == "__main__":
    # 1. 计算中心点 (25, 25)
    p_center = solve_laplace_at_point((25, 25))
    print(f"中心点 (25, 25) 的估计电势: {p_center:.2f} V")
    
    # 2. 计算靠近上边界的点 (25, 40)
    p_top = solve_laplace_at_point((25, 40))
    print(f"靠近上边界点 (25, 40) 的估计电势: {p_top:.2f} V")
