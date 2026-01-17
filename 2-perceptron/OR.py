import numpy as np


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    ans1 = OR(0, 0)
    ans2 = OR(1, 0)
    ans3 = OR(0, 1)
    ans4 = OR(1, 1)

    print(ans1, ans2, ans3, ans4)
