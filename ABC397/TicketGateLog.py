S = list(input())

res = 0
for i, s in enumerate(S):
    if i % 2 != 0 and s != 'o':
        S.insert(i, 'o')
        res += 1
    elif i % 2 == 0 and s != 'i':
        S.insert(i, 'i')
        res += 1
if len(S) % 2 != 0:
    res += 1
print(res)
