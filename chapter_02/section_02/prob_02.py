import sys


def resolve() -> None:
    N = int(sys.stdin.readline().strip())
    ST = [[0, 0] for _ in range(N)]
    for i in range(N):
        ST[i] = [int(x) for x in sys.stdin.readline().strip().split()]
    ST.sort(key=lambda x: x[1])
    ans = 0
    temp_t = 0
    for s, t in ST:
        if s > temp_t:
            ans += 1
            temp_t = t

    print(ans)


if __name__ == "__main__":
    resolve()
