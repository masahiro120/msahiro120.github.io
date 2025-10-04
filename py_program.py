def main():
    # import matplotlib. pyplot as pltimport numpy as np import pandas as pd from sklearn. svm import SVR from scipy.optimize import minimize
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.svm import SVR
    from scipy.optimize import minimize

    x = np.arange(1, 7)
    y = (x - 3.5) ** 2 + 1
    print("Dataframe:·n", pd.DataFrame({"Variable x": x,
    "Target y": y}))
    model = SVR(kernel="rbf"
    C=100,
    gamma=0.1, epsilon=0.1)
    model.fit(x.reshape(-1, 1), y)
    def func(x):
        return model.predict(x.reshape(-1, 1))
    result = minimize(func, x0=0)
    print("最小値のx：¥n", result.x[0])
    x_vals = np.linspace(1, 6, 100)
    y_vals = func(x_vals)
    plt.scatter(x, y, color="blue", label="Data")
    plt.plot(x_vals, y_vals, label="Prediction Curve", color="red")
    plt.scatter(result.x, func(result.x[0]), color="green", label="Optimal Solution")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()