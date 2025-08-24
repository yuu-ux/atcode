N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for j in range(N):
    ans += min(A[j], B[j])

for _ in range(Q):
    query = list(input().split())
    x = int(query[1])-1
    v = int(query[2])
    before = min(A[x], B[x])

    if query[0] == 'A':
        A[x] = v
    elif query[0] == 'B':
        B[x] = v

    after = min(A[x], B[x])
    ans += after - before
    print(ans)
