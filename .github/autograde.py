import pytest
import sys
import os

class GraderPlugin:
    def __init__(self):
        self.results = {}

    def pytest_runtest_logreport(self, report):
        if report.when == 'call':
            test_name = report.nodeid
            self.results[test_name] = report.passed

def main():
    plugin = GraderPlugin()
    print("⏳ 正在运行第13周自动测试 (蒙特卡洛与随机游走)...\n")
    
    # Run all tests
    test_paths = [
        'lab1_core/tests/test_core.py',
        'lab2_bonus/tests/test_bonus.py'
    ]
    
    pytest.main(test_paths + ['-q', '--tb=short'], plugins=[plugin])
    
    # Score allocation (Total 70 core + 30 bonus = 100)
    # Task A: 25, Task B: 25, Task C: 20 -> Sum 70
    # Bonus: 30
    
    # Mapping test functions to scores
    # lab1_core/tests/test_core.py::test_p1_radial_density (A)
    # lab1_core/tests/test_core.py::test_p2_pi_accuracy (B)
    # lab1_core/tests/test_core.py::test_p3_laplace_symmetry (C)
    # lab2_bonus/tests/test_bonus.py::test_heat_mc_initial_value (Bonus part)
    # lab2_bonus/tests/test_bonus.py::test_heat_mc_evolution (Bonus part)
    # lab2_bonus/tests/test_bonus.py::test_heat_mc_boundary (Bonus part)
    
    weights = {
        'test_p1_radial_density': 25.0,
        'test_p2_pi_accuracy': 25.0,
        'test_p3_laplace_symmetry': 20.0,
        'test_heat_mc': 30.0 # All tests in test_bonus.py starting with test_heat_mc
    }
    
    counts = {k: 0 for k in weights.keys()}
    passes = {k: 0 for k in weights.keys()}
    
    for nodeid, passed in plugin.results.items():
        matched = False
        for key in weights.keys():
            if key in nodeid:
                counts[key] += 1
                if passed:
                    passes[key] += 1
                matched = True
                break
                    
    total_base_score = 0.0
    bonus_score = 0.0
    
    summary_lines = ["### 🤖 自动评分结果 (GitHub Actions)"]
    summary_lines.append("| 任务模块 | 测试通过率 | 得分 | 满分 |")
    summary_lines.append("| :--- | :---: | :---: | :---: |")
    
    # Task A
    score_a = (passes['test_p1_radial_density'] / counts['test_p1_radial_density'] * 25.0) if counts['test_p1_radial_density'] > 0 else 0.0
    summary_lines.append(f"| Task A (电子云) | {passes['test_p1_radial_density']}/{counts['test_p1_radial_density']} | {score_a:.1f} | 25 |")
    
    # Task B
    score_b = (passes['test_p2_pi_accuracy'] / counts['test_p2_pi_accuracy'] * 25.0) if counts['test_p2_pi_accuracy'] > 0 else 0.0
    summary_lines.append(f"| Task B (MC 积分) | {passes['test_p2_pi_accuracy']}/{counts['test_p2_pi_accuracy']} | {score_b:.1f} | 25 |")
    
    # Task C
    score_c = (passes['test_p3_laplace_symmetry'] / counts['test_p3_laplace_symmetry'] * 20.0) if counts['test_p3_laplace_symmetry'] > 0 else 0.0
    summary_lines.append(f"| Task C (随机游走) | {passes['test_p3_laplace_symmetry']}/{counts['test_p3_laplace_symmetry']} | {score_c:.1f} | 20 |")
    
    # Bonus
    score_bonus = (passes['test_heat_mc'] / counts['test_heat_mc'] * 30.0) if counts['test_heat_mc'] > 0 else 0.0
    summary_lines.append(f"| Lab2 Bonus (热传导) | {passes['test_heat_mc']}/{counts['test_heat_mc']} | +{score_bonus:.1f} | +30 |")

    total_base_score = score_a + score_b + score_c
    
    summary_lines.append(f"\n**✅ 核心任务基础得分: {total_base_score:.1f} / 70.0**")
    summary_lines.append(f"**🚀 Bonus 挑战得分: +{score_bonus:.1f} / 30.0**")
    summary_lines.append(f"**🏆 最终自动评分总分: {total_base_score + score_bonus:.1f} / 100.0**")
    summary_lines.append("\n> *注：自动测试仅覆盖算法逻辑，最终成绩还包含实验报告中的物理分析、AI排雷质量及向量化实现评估。*")
    
    summary_text = "\n".join(summary_lines)
    print("\n" + "="*50)
    print(summary_text)
    print("="*50 + "\n")
    
    summary_file = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary_file:
        with open(summary_file, 'a', encoding='utf-8') as f:
            f.write(summary_text + "\n")
            
    sys.exit(0)

if __name__ == '__main__':
    main()
