N, M = map(int, input().split())
S = [list(map(int, input())) for _ in range(N)]

ans = [0] * N
for i in range(M):
    one = 0
    zero = 0
    for j in range(N):
        if S[j][i] == 1:
            one += 1
        elif S[j][i] == 0:
            zero += 1

    if one == 0 or zero == 0:
        for k in range(N):
            ans[k] += 1
    elif one > zero:
        for l in range(N):
            if S[l][i] == 0:
                ans[l] += 1
    elif one < zero:
        for m in range(N):
            if S[m][i] == 1:
                ans[m] += 1
max_ans = max(ans)
for i, v in enumerate(ans):
    if max_ans == v:
        print(i + 1, end=' ')
print('\n')
