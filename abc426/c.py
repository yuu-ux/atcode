N, Q = map(int, input().split())
PCs = [1] * (N+1)
PCs[0] = 0
o = 1
for i in range(Q):
    x, y = map(int, input().split())
    res = 0
    while o <= x:
        res += PCs[o]
        PCs[y] += PCs[o]
        o += 1
    print(res)
