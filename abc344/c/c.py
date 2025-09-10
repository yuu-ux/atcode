from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

note = defaultdict(int)
for i in range(N):
    for j in range(M):
        for k in range(L):
            note[A[i] + B[j] + C[k]] += 1
for i in range(Q):
    if note[X[i]] > 0:
        print('Yes')
    else:
        print('No')
