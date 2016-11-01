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

### 交差エントロピー誤差
正解ラベルが1に対応する自然対数を計算する。

```python
def cross_entropy_error(y, t):
    """交差エントロピー誤差"""
    delta = 1e-7
    cs = t * np.log(y + delta)
    return -np.sum(cs)
```

最小二乗誤差と違い、yとtの順番を間違えると正しく計算できない。


# memo


