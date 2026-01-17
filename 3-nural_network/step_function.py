import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# numpy配列の各要素に対して、それが0より大きいならTrue小さいならFlseを返す。
# それをdtypeで数値に変換
def step_function(x):
    return np.array(x > 0, dtype=np.int64)


# -5.0から5.0まで0.1刻みでnumpy配列を作る
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
