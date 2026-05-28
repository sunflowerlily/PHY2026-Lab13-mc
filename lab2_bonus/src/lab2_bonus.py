import numpy as np

def heat_time_reversal_mc(target_x=0.5, target_t=500, n_particles=10000):
    """
    Lab2 Bonus: 时间倒流蒙特卡洛求解一维热传导方程
    """
    results = []
    
    # 初始条件：0.4 <= x <= 0.6 为 100度，其余 0度
    def initial_temp(x):
        if 0.4 <= x <= 0.6:
            return 100.0
        return 0.0

    # TODO: 模拟 n_particles 个粒子
    # 每个粒子从 (target_x, target_t) 出发
    # 每次时间步减 1，空间位置随机向左或向右移一格 (dx = 1/100)
    # 当 t=0 时，读取初始温度并记录
    
    return 0.0

if __name__ == "__main__":
    print("开始模拟时间倒流热传导过程...")
    # 计算中心位置在不同时间步后的温度
    times = [0, 50, 200, 500]
    for t in times:
        temp = heat_time_reversal_mc(target_x=0.5, target_t=t, n_particles=5000)
        print(f"时间步 T = {t:3d}, 中心点温度估计: {temp:.2f} °C")
