import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic(A, B, C):
    # plotをクリア
    plt.clf()
    # x の範囲を決める（-10〜10を100点）
    x = np.linspace(-10, 10, 400)
    y = A * x**2 + B * x + C

    # グラフ描画
    # plt.figure(figsize=(6, 4))
    plt.plot(x, y, label=f"y = {A}x² + {B}x + {C}")
    plt.axhline(0, color="black", linewidth=0.8)  # x軸
    plt.axvline(0, color="black", linewidth=0.8)  # y軸
    plt.title("Quadratic Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_quadratic(a, b, c)