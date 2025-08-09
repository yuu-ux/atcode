N, K = map(int, input().split())
S = list(input())

cnt = 0
res = 0
for i in range(N):
    if S[i] == 'O':
        cnt += 1
    if cnt >= K:
        res += 1
        cnt = 0
    if S[i] == 'X':
        cnt = 0
print(res)
