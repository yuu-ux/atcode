N, M = map(int, input().split())

res = 0
limit = 10 ** 9
for i in range(M + 1):
    res += N ** i
    if res > limit:
        print('inf')
        exit()
print(res)
