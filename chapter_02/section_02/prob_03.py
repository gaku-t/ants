"""
Best Cow Line
"""

import sys


def resolve() -> None:
    N = int(sys.stdin.readline().strip())
    S = [x for x in sys.stdin.readline().strip()]
    left = 0
    right = N - 1
    T_list = [''] * N
    for i in range(N):
        if S[left:right+1] < S[left:right+1][::-1]:
            T_list[i] = S[left]
            left += 1
        else:
            T_list[i] = S[right]
            right -= 1

    print(''.join(T_list))


if __name__ == "__main__":
    resolve()
