"""
硬貨の問題
"""

import sys


def resolve() -> None:
    C_1, C_5, C_10, C_50, C_100, C_500 = (int(x) for x in sys.stdin.readline().strip().split())
    A = int(sys.stdin.readline().strip())
    ans = 0

    C = ((500, C_500), (100, C_100), (50, C_50), (10, C_10), (5, C_5), (1, C_1))
    for value, n in C:
        n_use = min(A // value, n)
        ans += n_use
        A -= value * n_use

    print(ans)


if __name__ == "__main__":
    resolve()
