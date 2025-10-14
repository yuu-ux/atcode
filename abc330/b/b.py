N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    if A[i] < L:
        ans.append(L)
    elif A[i] > R:
        ans.append(R)
    else:
        ans.append(A[i])
print(*ans)
