N, K = map(int, input().split())
A = list(map(int, input().split()))

everyone = K // N
mod = K % N

# 座標圧縮
sorted_A = sorted(A)
D = { v: i for i, v in enumerate(sorted_A) }
ans = {D[v]: everyone for v in A}

i = 0
while mod != 0:
    ans[i] += 1
    mod -= 1
    i += 1

for value in ans.values():
    print(value)
