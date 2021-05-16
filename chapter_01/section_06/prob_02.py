"""
Ants
"""

import sys


def resolve() -> None:
    L = int(sys.stdin.readline().strip())
    _ = int(sys.stdin.readline().strip())
    X = [int(x) for x in sys.stdin.readline().strip().split()]
    ans_min = max(min(x, L - x) for x in X)
    ans_max = max(max(x, L - x) for x in X)
    print(ans_min)
    print(ans_max)


if __name__ == "__main__":
    resolve()
