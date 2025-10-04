import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic(A, B, C, D, E):
    # print(f"関数: y = {A}x² + {B}x + {C}")
    # 改行なし
    print(f"関数: y = ", end=' ')
    if A ==1:
        print(f"x²", end=' ')
    elif A == -1:
        print(f"- x²", end=' ')
    elif A != 0:
        print(f"{A}x²", end=' ')
    if B != 0:
        if B == 0:
            pass
        elif B > 0:
            print(f"+ {B}x", end=' ')
        else:
            print(f"- {abs(B)}x", end=' ')
    if C != 0:
        if C == 0:
            pass
        elif C > 0:
            print(f"+ {C}", end=' ')
        else:
            print(f"- {abs(C)}", end=' ')
    print()  # 改行
    print(f"x の範囲: {D} 〜 {E}")
    # plotをクリア
    plt.clf()
    # x の範囲を決める（-10〜10を100点）
    # x = np.linspace(-10, 10, 400)
    x = np.linspace(D, E, 400)
    y = A * x**2 + B * x + C

    axle = -B / (2 * A)
    if D < axle < E and A > 0:
        x_max = E if axle - D < E - axle else D
        x_min = axle
        y_max = A * x_max**2 + B * x_max + C
        y_min = A * x_min**2 + B * x_min + C
    elif D < axle < E and A < 0:
        x_min = E if axle - D < E - axle else D
        x_max = axle
        y_min = A * x_min**2 + B * x_min + C
        y_max = A * x_max**2 + B * x_max + C
    elif axle <= D:
        x_max = E if A > 0 else D
        x_min = D if A > 0 else E
        y_max = A * x_max**2 + B * x_max + C
        y_min = A * x_min**2 + B * x_min + C
    elif axle >= E:
        x_max = D if A > 0 else E
        x_min = E if A > 0 else D
        y_max = A * x_max**2 + B * x_max + C
        y_min = A * x_min**2 + B * x_min + C

    print(f"最大値: x = {x_max}, y = {y_max}")
    print(f"最小値: x = {x_min}, y = {y_min}")
    
    x_range = E - D
    y_range = y_max - y_min
    x_mid = (D + E) / 2
    y_mid = (y_max + y_min) / 2
    
    # グラフ描画
    
    # 座標平面の設定
    plt.xlim(x_mid - x_range*0.6, x_mid + x_range*0.6)
    plt.ylim(y_mid - y_range*0.6, y_mid + y_range*0.6)
    
    plt.plot(x, y, label=f"y = {A}x² + {B}x + {C}")
    
    plt.axhline(0, color="black", linewidth=0.8)  # x軸
    plt.axvline(0, color="black", linewidth=0.8)  # y軸
    
    plt.axvline(D, color="red", linestyle="--", label=f"x = {D}")
    plt.axvline(E, color="blue", linestyle="--", label=f"x = {E}")
    
    plt.scatter([x_max], [y_max], color="red", zorder=5)
    plt.scatter([x_min], [y_min], color="blue", zorder=5)
    
    plt.title("Quadratic Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_quadratic(a, b, c, d, e)