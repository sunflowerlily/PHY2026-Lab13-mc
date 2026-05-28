import pytest
import numpy as np
import sys
import os

# 将 src 加入路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from p1_electron_cloud import hydrogen_radial_density
from p2_mc_integration import hit_or_miss_pi, mean_value_pi, importance_sampling_pi
from p3_random_walk_laplace import solve_laplace_at_point

def test_p1_radial_density():
    # 测试径向分布函数的基本性质
    assert hydrogen_radial_density(0.0529) > 0
    assert hydrogen_radial_density(0) == 0

def test_p2_pi_accuracy():
    # L1 基础测试：三种方法算出的 PI 是否都在合理范围内
    # 给定较大的容差，因为 MC 有随机性
    tol = 0.1
    assert abs(hit_or_miss_pi(10000) - np.pi) < tol
    assert abs(mean_value_pi(10000) - np.pi) < tol
    # 只要学生实现了，重要性采样的方差应该更小，此处仅测基本正确性
    res_is = importance_sampling_pi(10000)
    assert res_is is not None
    assert abs(res_is - np.pi) < tol

def test_p3_laplace_symmetry():
    # 测试中心点 (25, 25) 的电势
    # 根据对称性，上边界100，其余0，中心点电势应接近 (100+0+0+0)/4 = 25V
    # 考虑随机误差，容差设为 5V
    potential = solve_laplace_at_point((25, 25), n_particles=1000)
    assert 20 <= potential <= 30
