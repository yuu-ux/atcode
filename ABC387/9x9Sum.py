N = int(input())

res = 0
for i in range(1, 10):
    for j in range(1, 10):
        temp = i * j
        if temp != N:
            res += temp
print(res)
