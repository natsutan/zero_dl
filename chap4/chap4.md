# ニューラルネットワークの学習
---
## 損失関数
NNにおける評価関数のこと。小さいほうが良い。

### 最小二乗誤差

```python
def mean_squared_error(y, t):
    """最小二乗誤差を求める"""
    return 0,5 * np.sum((y-t)**2)
```

# memo


