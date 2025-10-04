import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic(A, B, C, N, M):
    func = "y = "
    conp_square = func
    if A == 1:
        func += "x² "
    elif A == -1:
        func += "- x² "
    elif A != 0:
        func += f"{A}x² "
    if B != 0:
        if B == 0:
            pass
        elif B > 0:
            func += f"+ {B}x "
        else:
            func += f"- {abs(B)}x "
    if C != 0:
        if C == 0:
            pass
        elif C > 0:
            func += f"+ {C} "
        else:
            func += f"- {abs(C)} "
    print(f"関数　　　 : {func}")

    if B/(2*A) != 0:
        if A == 1:
            conp_square += "(x "
        elif A == -1:
            conp_square += "-(x "
        elif A != 0:
            conp_square += f"{A}(x "
        if B/(2*A) > 0:
            conp_square += f"+ {B/(2*A)})²"
        elif B/(2*A) < 0:
            conp_square += f"- {abs(B/(2*A))})²"
    else:
        if A == 1:
            conp_square += "x²"
        elif A == -1:
            conp_square += "-x²"
        elif A != 0:
            conp_square += f"{A}x²"
    if C - (B**2)/(4*A) > 0:
        conp_square += f" + {C - (B**2)/(4*A)}"
    elif C - (B**2)/(4*A) < 0:
        conp_square += f" - {abs(C - (B**2)/(4*A))}"
    print(f"平方完成後 : {conp_square}")

    # plotをクリア
    plt.clf()
    # x の範囲を決める（-10〜10を100点）
    # x = np.linspace(-10, 10, 400)
    x = np.linspace(N, M, 400)
    y = A * x**2 + B * x + C

    axle = -B / (2 * A)
    if N < axle < M and A > 0:
        x_max = M if axle - N < M - axle else N
        x_min = axle
        y_max = A * x_max**2 + B * x_max + C
        y_min = A * x_min**2 + B * x_min + C
    elif N < axle < M and A < 0:
        x_min = M if axle - N < M - axle else N
        x_max = axle
        y_min = A * x_min**2 + B * x_min + C
        y_max = A * x_max**2 + B * x_max + C
    elif axle <= N:
        x_max = M if A > 0 else N
        x_min = N if A > 0 else M
        y_max = A * x_max**2 + B * x_max + C
        y_min = A * x_min**2 + B * x_min + C
    elif axle >= M:
        x_max = N if A > 0 else M
        x_min = M if A > 0 else N
        y_max = A * x_max**2 + B * x_max + C
        y_min = A * x_min**2 + B * x_min + C

    print(f"最大値　　 : ({x_max:.1f}, {y_max:.1f})")
    print(f"最小値　　 : ({x_min:.1f}, {y_min:.1f})")

    x_range = M - N
    y_range = y_max - y_min
    x_mid = (N + M) / 2
    y_mid = (y_max + y_min) / 2
    
    # グラフ描画
    # 座標平面の設定
    plt.xlim(x_mid - x_range*0.6, x_mid + x_range*0.6)
    plt.ylim(y_mid - y_range*0.6, y_mid + y_range*0.6)
    
    plt.plot(x, y, label=func)
    
    plt.axhline(0, color="black", linewidth=0.8)  # x軸
    plt.axvline(0, color="black", linewidth=0.8)  # y軸
    
    plt.axvline(N, color="gray", linestyle="--")
    plt.axvline(M, color="gray", linestyle="--")
    
    plt.scatter([x_max], [y_max], color="red", zorder=5, label="Max")
    plt.scatter([x_min], [y_min], color="blue", zorder=5, label="Min")

    plt.title("Quadratic Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_quadratic(a, b, c, n, m)