N, A = map(int, input().split())
T = list(map(int, input().split()))

cnt = 0
for i in range(N):
    now = T.pop(0)
    if cnt < now:
        cnt += now - cnt
    cnt += A
    print(cnt)

