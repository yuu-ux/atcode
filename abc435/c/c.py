N = int(input())
A = list(map(int, input().split()))

r = 0
i = 0
while i <= r and i < N:
    r = max(r, i + A[i] - 1)
    i += 1

print(min(N, r + 1))
