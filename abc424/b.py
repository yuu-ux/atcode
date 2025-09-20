from collections import defaultdict

N, M, K = map(int, input().split())
ans = defaultdict(int)

res = []
for _ in range(K):
    a, _ = map(int, input().split())
    ans[a] += 1
    for i in range(1, N+1):
        if ans[i] == M:
            res.append(i)
            ans[i] = -99999
print(*res)

# N = 3, M =3 の場合
# 1: 3
# 2: 3
# 3: 3
# 人 N 分 1: 3

