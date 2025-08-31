N = int(input())
A = list(map(int, input().split()))

ans = [0] * (N+1)
for i in range(N):
    ans[i+1] = ans[i] + A[i]

# A1 + A2 = [1, 3)
# A1 + A3 = [1, )
# A2 + A3
