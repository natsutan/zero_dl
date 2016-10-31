# 3章メモ
---
## 活性化関数
---
### STEP関数
入力が0を超えたら１、それ以外は0

```python
def step_function(x):
    # x > 0 が真偽値を返し、dtypeでintを指定して0と1に変換している
    return np.array(x > 0, dtype=np.int)
```

![step関数](./step.png "step関数")

### sigmoid関数
非線形であることが大事。線形であるばあい、多層のメリットがだせない。

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

![sigmoid関数](./sigmoid.png "sigmoid関数")

### ReLU関数
Rectified Linear Unit  

```python
def relu(x):
    return np.maximum(0, x)
```

![ReLU関数](./relu.png "ReLU関数")
---
### memo
出力層で利用する活性化関数は、解く問題の性質に応じて決める。回帰問題では恒等関数、2クラス分類ではシグモイド、多クラス分類ではソフトマックスを使うのが一般的。

## 出力層

### softmax関数

定義のまま実装するとオーバーフローが発生する。
```python
def softmax_bad(a):
    """駄目なsoftmaxの実装"""
    return np.exp(a) / np.sum(np.exp(a))

a = np.array([1010, 1000, 990])
c = softmax_bad(a)
print(c) # [ nan  nan  nan]
```

最大値を引くことでオーバーフローを防ぐ。なぜ最大値を引いてもOKかは本に記載。

```python
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
```

### memo
softmax関数では入力と出力の大小関係は変化しない。出力層にsoftmaxを使うのは学習の効率を高めるため。識別時には一番大きい値を選べばよいので、出力層のsoftmax関数は省略できる。
