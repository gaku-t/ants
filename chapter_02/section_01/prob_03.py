"""
迷路の最短路
"""

import sys
from collections import deque


def resolve() -> None:
    R, C = (int(x) for x in sys.stdin.readline().strip().split())
    maze = [[''] * C for _ in range(R)]
    for i in range(R):
        maze[i] = [x for x in sys.stdin.readline().strip()]

    start = (-1, -1)
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'S':
                start = (i, j)
                maze[i][j] = '#'
                break
        else:
            continue
        break

    queue = deque([start])
    ans = 0
    while queue:
        ans += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            neighbors = (
                (i+1, j),
                (i-1, j),
                (i, j+1),
                (i, j-1),
            )
            for ni, nj in neighbors:
                if 0 <= ni < R and 0 <= nj < C:
                    if maze[ni][nj] == 'G':
                        print(ans)
                        return
                    elif maze[ni][nj] == '.':
                        queue.append((ni, nj))
                        maze[ni][nj] = '#'


if __name__ == "__main__":
    resolve()
