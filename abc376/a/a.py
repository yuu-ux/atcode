N, C = map(int, input().split())
T = list(map(int, input().split()))

res = 1
candy_get_time = T[0]
for i in range(1, N):
    if (T[i] - candy_get_time) >= C:
        res += 1
        candy_get_time = T[i]
print(res)
