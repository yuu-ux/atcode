N, Q = map(int, input().split())
X = list(map(int, input().split()))

boxs = [0] * N
res = []
for i in X:
    if i >= 1:
        boxs[i - 1] += 1
        res.append(i)
    elif i == 0:
        index = boxs.index(min(boxs))
        boxs[index] += 1
        res.append(index + 1)
print(*res)
