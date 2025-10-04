import numpy as np
import matplotlib.pyplot as plt

def print_func(A, B, C):
    func = "y = "
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

def complete_square(A, B, C):
    P = B / (2 * A)
    Q = C - (B**2) / (4 * A)
    return P, Q

def print_complete_square(A, P, Q):
    func = "y = "
    if P != 0:
        if A == 1:
            func += "(x "
        elif A == -1:
            func += "-(x "
        elif A != 0:
            func += f"{A}(x "
    else:
        if A == 1:
            func += "x² "
        elif A == -1:
            func += "-x² "
        elif A != 0:
            func += f"{A}x² "
    if P > 0:
        func += f"- {P})²"
    elif P < 0:
        func += f"+ {abs(P)})²"
    if Q > 0:
        func += f" + {Q}"
    elif Q < 0:
        func += f" - {abs(Q)}"
    print(f"平方完成後 : {func}")
    return func

def plot_quadratic(A, P, Q, N, M, func):
    # plotをクリア
    plt.clf()
    x = np.linspace(N, M, 400)
    y = A * (x - P)**2 + Q

    if N < P < M and A > 0:
        x_max = M if P - N < M - P else N
        y_max = A * (x_max - P)**2 + Q
        x_min = P
        y_min = Q
    elif N < P < M and A < 0:
        x_max = P
        y_max = Q
        x_min = M if P - N < M - P else N
        y_min = A * (x_min - P)**2 + Q
    elif P <= N:
        x_max = M if A > 0 else N
        y_max = A * (x_max - P)**2 + Q
        x_min = N if A > 0 else M
        y_min = A * (x_min - P)**2 + Q
    elif P >= M:
        x_max = N if A > 0 else M
        y_max = A * (x_max - P)**2 + Q
        x_min = M if A > 0 else N
        y_min = A * (x_min - P)**2 + Q


    x_range = M - N
    y_range = y_max - y_min
    x_mid = (N + M) / 2
    y_mid = (y_max + y_min) / 2
    
    if x_mid == P:
        if A > 0:
            print(f"最大値　　 : ({x_max:.1f}, {y_max:.1f}), ({x_max+x_range:.1f}, {y_max:.1f})")
            print(f"最小値　　 : ({x_min:.1f}, {y_min:.1f})")
            plt.scatter([x_max], [y_max], color="red", zorder=5, label="Max")
            plt.scatter([x_max+x_range], [y_max], color="red", zorder=5)
            plt.scatter([x_min], [y_min], color="blue", zorder=5, label="Min")
        else: 
            print(f"最大値　　 : ({x_max:.1f}, {y_max:.1f})")
            print(f"最小値　　 : ({x_min:.1f}, {y_min:.1f}), ({x_min+x_range:.1f}, {y_min:.1f})")
            plt.scatter([x_max], [y_max], color="red", zorder=5, label="Max")
            plt.scatter([x_min], [y_min], color="blue", zorder=5, label="Min")
            plt.scatter([x_min+x_range], [y_min], color="blue", zorder=5)
    else:
        print(f"最大値　　 : ({x_max:.1f}, {y_max:.1f})")
        print(f"最小値　　 : ({x_min:.1f}, {y_min:.1f})")
        plt.scatter([x_max], [y_max], color="red", zorder=5, label="Max")
        plt.scatter([x_min], [y_min], color="blue", zorder=5, label="Min")

    
    # グラフ描画
    # 座標平面の設定
    plt.xlim(x_mid - x_range*0.6, x_mid + x_range*0.6)
    plt.ylim(y_mid - y_range*0.6, y_mid + y_range*0.6)
    
    plt.plot(x, y, label=func)
    
    plt.axhline(0, color="black", linewidth=0.8)  # x軸
    plt.axvline(0, color="black", linewidth=0.8)  # y軸
    
    plt.axvline(N, color="gray", linestyle="--")
    plt.axvline(M, color="gray", linestyle="--")
    

    plt.title("Quadratic Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    if func_type == "abc":
        print_func(a, b, c)
        p, q = complete_square(a, b, c)
    func = print_complete_square(a, p, q)
    plot_quadratic(a, p, q, n, m, func)