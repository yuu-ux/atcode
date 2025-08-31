X, Y = map(int, input().split())

ans = []
for n in range(1, 11):
    if n == 1:
        ans.append(X)
    elif n == 2:
        ans.append(Y)
    else:
        cur = ans[n-2] + ans[n-3]
        if cur >= 10:
            ans.append(int(''.join(reversed(str(cur)))))
            continue
        ans.append(ans[n-2] + ans[n-3])
print(ans[9])
