S = list(input())
N = len(S)

ans = 0
for r in range(N):
    for l in range(0, r-1):
        if S[l] != 't' or S[r] != 't':
            continue
        cnt = 0
        _len = r - l - 1
        for k in range(l+1, r):
            if S[k] == 't':
                cnt += 1
        now = cnt / _len
        ans = max(ans, now)
print(ans)
