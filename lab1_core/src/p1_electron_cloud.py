import numpy as np
import matplotlib.pyplot as plt

def hydrogen_radial_density(r, a=0.0529):
    """
    氢原子基态径向概率密度函数 D(r)
    """
    return (4 * r**2 / a**3) * np.exp(-2 * r / a)

def rejection_sampling_electron(n_points=10000, r_max=0.25):
    """
    任务 A：使用舍选抽样法生成电子云径向分布
    """
    # TODO: 找到 D(r) 在 [0, r_max] 上的最大值 D_max
    # TODO: 向量化生成候选点 r1, r2
    # TODO: 筛选满足条件的点
    # TODO: 返回有效半径数组 r_samples
    return np.array([]) # 临时返回空数组

def project_to_2d(r_samples):
    """
    任务 A：将径向分布转化为二维平面分布 (x, y)
    """
    # TODO: 随机生成角度 theta
    # TODO: 坐标变换 x = r*cos(theta), y = r*sin(theta)
    return np.array([]), np.array([])

if __name__ == "__main__":
    # 运行展示
    print("正在生成电子云分布...")
    r_samples = rejection_sampling_electron(n_points=20000)
    
    if len(r_samples) > 0:
        x, y = project_to_2d(r_samples)
        
        plt.figure(figsize=(6, 6))
        plt.scatter(x, y, s=1, alpha=0.3, color='blue')
        plt.title("Hydrogen Atom Electron Cloud (Ground State)")
        plt.xlabel("x (nm)")
        plt.ylabel("y (nm)")
        plt.axis('equal')
        plt.show()
    else:
        print("请先完成 rejection_sampling_electron 函数以查看可视化结果。")
