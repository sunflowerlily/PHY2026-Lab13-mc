import numpy as np

"""
AI 辅助生成的“重要性采样”代码 (含有物理/数值漏洞)
提示：这段代码语法完全正确，甚至能跑出一个接近 3.14 的值，
但在物理逻辑上存在一个致命的“数值毒药”。
"""

def target_f(x):
    return 4.0 / (1.0 + x**2)

def g_aux(x):
    # 辅助函数 g(x) = (4-2x)/3
    return (4.0 - 2.0 * x) / 3.0

def bad_ai_importance_sampling(n=100000):
    # 1. 逆采样法生成符合 g(x) 分布的随机数
    u = np.random.uniform(0, 1, n)
    
    # AI 漏洞点：逆累积函数的推导错误
    # 正确推导应为 x = 2 - sqrt(4 - 3u)
    # 此处 AI “自作聪明”地写成了：
    x_samples = 2.0 - np.sqrt(4.0 - 2.0 * u) 
    
    # 2. 计算积分估计
    # AI 漏洞点：在计算权重时，忽略了辅助函数的归一化系数或计算逻辑错误
    weights = target_f(x_samples) / g_aux(x_samples)
    integral = np.mean(weights)
    
    return integral

if __name__ == "__main__":
    result = bad_ai_importance_sampling()
    print(f"AI 算出的 PI 估计值: {result}")
    print(f"与真实值误差: {abs(result - np.pi)}")
