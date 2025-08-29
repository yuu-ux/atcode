from collections import Counter
N = int(input())
A = list(map(int, input().split()))

S = [0] * (N+1)
for i in range(N):
    S[i+1] += S[i] + A[i]

ans = 0
for _, v in Counter(S).items():
    ans += v * (v - 1) // 2
print(ans)
