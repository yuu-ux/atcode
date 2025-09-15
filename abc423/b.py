N = int(input())
L = list(map(int, input().split()))

left_cnt = 1
right_cnt = 1

for l in L:
    if l != 1:
        left_cnt += 1
    else:
        break

for i in range(N-1, -1, -1):
    if L[i] != 1:
        right_cnt += 1
    else:
        break

if left_cnt + right_cnt >= (N+1):
    print(0)
else:
    print((N+1)-(left_cnt + right_cnt))
