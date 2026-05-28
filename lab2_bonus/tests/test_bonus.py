import pytest
import numpy as np
import sys
import os

# 将 src 加入路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab2_bonus import heat_time_reversal_mc

def test_heat_mc_initial_value():
    """
    测试时间步为 0 时的温度。
    从 (0.5, 0) 出发，应该直接返回初始温度 100。
    """
    temp = heat_time_reversal_mc(target_x=0.5, target_t=0, n_particles=100)
    assert temp == 100.0

def test_heat_mc_evolution():
    """
    测试时间演化后的温度。
    中心点温度应该随着时间步增加而逐渐下降（热扩散）。
    """
    # 模拟 10 个时间步后的温度
    temp_early = heat_time_reversal_mc(target_x=0.5, target_t=10, n_particles=1000)
    # 模拟 200 个时间步后的温度
    temp_late = heat_time_reversal_mc(target_x=0.5, target_t=200, n_particles=1000)
    
    # 物理直觉：中心点温度应下降
    assert temp_late < temp_early
    # 且应在 0 到 100 之间
    assert 0 <= temp_late <= 100

def test_heat_mc_boundary():
    """
    测试靠近边界处的温度。
    靠近 x=0 或 x=1 且时间较短时，温度应接近 0。
    """
    temp_edge = heat_time_reversal_mc(target_x=0.1, target_t=10, n_particles=500)
    assert temp_edge < 10.0
