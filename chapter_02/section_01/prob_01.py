"""
部分和問題
"""

import sys


def resolve() -> None:
    N = int(sys.stdin.readline().strip())
    A = [int(x) for x in sys.stdin.readline().strip().split()]
    K = int(sys.stdin.readline().strip())
    for i in range(1 << N):
        ki = 0
        for j in range(N):
            if (i >> j) & 1 == 1:
                ki += A[j]
        if ki == K:
            print('Yes')
            return
    print('No')


if __name__ == "__main__":
    resolve()
