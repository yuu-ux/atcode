S = str(input())
res = 0
i = 0

while res != 1:
    res = 0
    for s in S:
        temp = pow(int(s), 2)
        res += temp
    S = str(res)
    i += 1
    if i > 10000:
        print('No')
        exit()
print('Yes')
