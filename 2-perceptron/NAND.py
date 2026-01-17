import numpy as np


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    ans1 = NAND(0, 0)
    ans2 = NAND(1, 0)
    ans3 = NAND(0, 1)
    ans4 = NAND(1, 1)

    print(ans1, ans2, ans3, ans4)
