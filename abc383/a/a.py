N = int(input())
query = [list(map(int, input().split())) for _ in range(N)]

res = query[0][1]
for i in range(1, N):
    delay = query[i][0] - query[i-1][0]
    res -= delay
    if res < 0:
        res = 0
    res += query[i][1]
print(res)

