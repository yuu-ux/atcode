from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

table = defaultdict(int)
for i, v in enumerate(A):
    table[v] = i+1

ans = []
ans.append(A.index(-1) + 1)
for i in range(N-1):
    ans.append(table[ans[i]])
print(*ans)
