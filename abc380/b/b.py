S = list(input())
res = []
cnt = 0

for s in S:
    if s == '|':
        if cnt != 0:
            res.append(cnt)
        cnt = 0
        continue
    if s == '-':
        cnt += 1
print(*res)

