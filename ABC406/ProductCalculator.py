N, K = map(int, input().split())
A = list(map(int, input().split()))

res = 1
for a in A:
    res *= a
    if len(str(res)) > K:
        res = 1
print(res)
