S = list(input())
ans = []
flg_shape = True
for i in range(len(S)):
    if S[i] == '#':
        ans.append('#')
        flg_shape = True
    elif flg_shape:
        ans.append('o')
        flg_shape = False
    else:
        ans.append('.')
print(*ans, sep='')
