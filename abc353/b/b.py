N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 1
cur_k = K
while A:
    if cur_k >= A[0]:
        cur_k -= A.pop(0)
    else:
        cnt += 1
        cur_k = K
print(cnt)
