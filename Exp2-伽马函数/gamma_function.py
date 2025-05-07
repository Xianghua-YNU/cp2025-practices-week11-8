import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import fixed_quad


# 定义伽马函数的被积函数
def f(x, a):
    return x**(a - 1) * np.exp(-x)


# 绘制被积函数图像
def plot_integrand():
    x = np.linspace(0, 5, 400)
    for a in [2, 3, 4]:
        y = f(x, a)
        plt.plot(x, y, label=f'a = {a}')
    plt.xlabel('x')
    plt.ylabel('f(x, a)')
    plt.title('Gamma Function Integrand')
    plt.legend()
    plt.grid(True)
    plt.show()


# 定义变换后的被积函数
def g(z, a):
    c = a - 1
    return np.exp((a - 1) * np.log(c * z / (1 - z)) - c * z / (1 - z)) * c / (1 - z)**2


# 计算伽马函数的值
def gamma_function(a):
    result, _ = fixed_quad(g, 0, 1, args=(a,), n=10)
    return result


# 运行实验
if __name__ == "__main__":
    # 绘制被积函数图像
    plot_integrand()

    # 计算 Γ(1.5)
    gamma_1_5_calculated = gamma_function(1.5)
    gamma_1_5_exact = np.sqrt(np.pi) / 2
    relative_error_1_5 = np.abs((gamma_1_5_calculated - gamma_1_5_exact) / gamma_1_5_exact)

    # 计算整数 Γ(a)
    integers = [3, 6, 10]
    for a in integers:
        gamma_calculated = gamma_function(a)
        gamma_exact = np.math.factorial(a - 1)
        relative_error = np.abs((gamma_calculated - gamma_exact) / gamma_exact)
        print(f"a = {a}:")
        print(f"  计算值 Γ(a): {gamma_calculated}")
        print(f"  精确值 (a-1)!: {gamma_exact}")
        print(f"  相对误差: {relative_error}")

    print("Γ(1.5):")
    print(f"  计算值: {gamma_1_5_calculated}")
    print(f"  精确值 (√π/2): {gamma_1_5_exact}")
    print(f"  相对误差: {relative_error_1_5}")
    
