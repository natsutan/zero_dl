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

### なぜ損失関数を設定するのか？
学習で使うときに傾きが必要。認識制度を指標とすると、パラメータの微分がほとんどの場所で0になるから。

## 数値微分

駄目な例。前方差分

```python
def numerical_diff(f, x):
    h = 10e-50
    return (f(x+h) - f(x)) / h
```

h を0.0001にすると良いと分かっている。さらに中心差分に変更。

```python
def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-x)) / (2*h)
```

## 数値微分の例
$ y = 0.01x^2 + 0.1x $


# memo


