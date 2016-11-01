import numpy as np


def cross_entropy_error(y, t):
    """交差エントロピー誤差"""
    delta = 1e-7
    cs = t * np.log(y + delta)
    return -np.sum(cs)

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

#あまり近くない
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
cee = cross_entropy_error(np.array(y), np.array(t))
print(cee)

# 近い
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.5, 0.0]
cee = cross_entropy_error(np.array(y), np.array(t))
print(cee)
