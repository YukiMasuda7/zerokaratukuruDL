import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# X[i]はi番目の入力
# W1[i][j]は0層目のi番目の要素から1層目のj番目の要素に伝達する時に掛ける重み
# B1[i]は1層目のi番目の要素に足されるバイアス。1層目の要素はX・W1で1*3の形状の行列になることに注意。
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
# A1は活性化関数を通す前の値
# Z1は活性化関数(今回はシグモイド)を通した後の値
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)

print(A1)
print(Z1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)


# 恒等関数(出力層の活性化関数)
def identity_function(x):
    return x


W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)

print(Y)
