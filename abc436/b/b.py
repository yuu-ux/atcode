N = int(input())
res = [[0] * N for _ in range(N)]

r = 0
c = (N-1)//2
k = 1
res[r][c] = k
for _ in range(N ** 2 - 1):
    r_index = (r-1) % N
    c_index = (c + 1) % N
    if res[r_index][c_index] == 0:
        res[r_index][c_index] = k + 1
        r = r_index
        c = c_index
    else:
        res[(r + 1) % N][c] = k + 1
        r = (r + 1) % N
    k += 1


for r in res:
    print(*r)
