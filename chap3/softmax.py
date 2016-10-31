import numpy as np

def softmax_bad(a):
    """駄目なsoftmaxの実装"""
    return np.exp(a) / np.sum(np.exp(a))


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

a = np.array([1010, 1000, 990])
c = softmax_bad(a)
print(c) # [ nan  nan  nan]

c = softmax(a)
print(c)