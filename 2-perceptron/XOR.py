# XORはAND, NAND, ORの組み合わせ
# 単層パーセプトロンでは表せなかった表現を多層パーセプトロンで表せる
from AND import AND
from NAND import NAND
from OR import OR


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


if __name__ == "__main__":
    ans1 = XOR(0, 0)
    ans2 = XOR(1, 0)
    ans3 = XOR(0, 1)
    ans4 = XOR(1, 1)

    print(ans1, ans2, ans3, ans4)
