
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(key=lambda x: ((x ^ k).bit_count(), x))

    print(*arr)


t = int(input())

for _ in range(t):
    solve()
