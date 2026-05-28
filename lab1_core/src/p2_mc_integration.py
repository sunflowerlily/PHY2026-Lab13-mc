import numpy as np
import matplotlib.pyplot as plt

def target_function(x):
    """待积分函数 f(x) = 4 / (1 + x^2)"""
    return 4 / (1 + x**2)

def hit_or_miss_pi(n_points=100000):
    """
    境界一：投点法
    """
    # TODO: 在 [0,1]x[0,4] 内投点并统计落在曲线下方的比例
    return 0.0

def mean_value_pi(n_points=100000):
    """
    境界二：平均值法
    """
    # TODO: 利用积分中值定理采样
    return 0.0

def importance_sampling_pi(n_points=100000):
    """
    境界三：重要性采样
    使用 g(x) = (4-2x)/3 作为辅助函数
    """
    # TODO: 逆采样法生成符合 g(x) 的随机数 x
    # TODO: 计算积分估计值
    return 0.0

if __name__ == "__main__":
    N = 100000
    print(f"使用 N = {N} 进行计算：")
    
    pi1 = hit_or_miss_pi(N)
    pi2 = mean_value_pi(N)
    pi3 = importance_sampling_pi(N)
    
    print(f"投点法 PI: {pi1:.6f} (误差: {abs(pi1-np.pi):.6e})")
    print(f"均值法 PI: {pi2:.6f} (误差: {abs(pi2-np.pi):.6e})")
    print(f"重要性采样 PI: {pi3:.6f} (误差: {abs(pi3-np.pi):.6e})")
    
    # 可选：绘制误差随 N 变化的曲线
    # ns = np.logspace(2, 5, 10).astype(int)
    # ...
