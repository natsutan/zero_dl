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
