from collections import Counter
N, M = map(int, input().split())
A = Counter(map(int, input().split()))

res = []
cnt = 0
for i in range(1, N + 1):
    if A[i] != 1:
        res.append(i)
        cnt += 1
print(cnt)
print(*res)

