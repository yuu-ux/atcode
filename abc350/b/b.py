N, Q = map(int, input().split())
A = list(map(int, input().split()))
tooth = [True for _ in range(N)]
for i in range(Q):
    index = A[i] - 1
    if tooth[index] == True:
        tooth[index] = False
    else:
        tooth[index] = True
print(sum(a for a in tooth if a == True))
