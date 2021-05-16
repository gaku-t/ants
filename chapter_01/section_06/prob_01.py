"""
三角形
"""

import math
import sys
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
from itertools import chain, combinations, combinations_with_replacement, permutations
from typing import Callable, Dict, List, NamedTuple, Optional, Tuple


def resolve() -> None:
    N = int(sys.stdin.readline().strip())
    A = [int(x) for x in sys.stdin.readline().strip().split()]

    ans = 0
    for i in range(1, N - 1):
        sum_2_edges = A[i] + A[i-1]
        low = i + 1
        high = N - 1
        if A[high] < sum_2_edges:
            ans = max(ans, A[high] + sum_2_edges)
            continue
        elif A[low] >= sum_2_edges:
            continue
        while low + 1 < high:
            mid = (low + high) // 2
            if A[mid] < sum_2_edges:
                low = mid
            else:
                high = mid
        ans = max(ans, A[low] + sum_2_edges)

    print(ans)


if __name__ == "__main__":
    resolve()

