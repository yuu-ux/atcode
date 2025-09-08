N, K = map(int, input().split())
A = set(map(int, input().split()))

ans = K * (K + 1) // 2
for a in A:
    if a <= K:
        ans -= a
print(ans)
