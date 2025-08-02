N, Q = map(int, input().split())

L = [list(map(int, input().split())) for _ in range(N)]
S = [list(map(int, input().split())) for _ in range(Q)]

for i in range(N):
    _, *a = map(int, input().split())
    A[i] = a

for i in range(Q):
    s, t = (S[i][0]-1), S[i][1]
    print(L[s][t])
