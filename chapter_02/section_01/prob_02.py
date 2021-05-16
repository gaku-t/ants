"""
Lake Counting
"""

import sys


def resolve() -> None:
    R, C = (int(x) for x in sys.stdin.readline().strip().split())
    X = [[''] * C for _ in range(R)]
    for i in range(R):
        X[i] = [x for x in sys.stdin.readline().strip()]

    ans = 0
    for i in range(R):
        for j in range(C):
            if X[i][j] == '.':
                continue
            ans += 1
            stack = [(i, j)]
            X[i][j] = '.'
            while stack:
                x, y = stack.pop()
                neighbors = (
                    (x-1, y-1),
                    (x-1, y),
                    (x-1, y+1),
                    (x, y-1),
                    (x, y+1),
                    (x+1, y-1),
                    (x+1, y),
                    (x+1, y+1),
                )
                for nx, ny in neighbors:
                    if 0 <= nx < R and 0<= ny < C and X[nx][ny] == 'W':
                        stack.append((nx, ny))
                        X[nx][ny] = '.'

    print(ans)


if __name__ == "__main__":
    resolve()
