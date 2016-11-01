import numpy as np

def mean_squared_error(y, t):
    """最小二乗誤差を求める"""
    return 0,5 * np.sum((y-t)**2)

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

#あまり近くない
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
mse = mean_squared_error(np.array(y), np.array(t))
print(mse)

# 近い
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.5, 0.0]
mse = mean_squared_error(np.array(y), np.array(t))
print(mse)
