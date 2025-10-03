from collections import deque

N, Q = map(int, input().split())
A = list(map(int, input().split()))
dq = deque(A)
# 2 * 10^5
for i in range(Q):
    query = list(map(int, input().split()))
    ans = 0
    if query[0] == 1:
        # 先頭要素を末尾へ
        c = query[1]
        # 2 * 10^5
        for j in range(c):
            dq.append(dq.popleft())
    else:
        l, r = query[1]-1, query[2]
        # 2 * 10^5
        for j in range(l, r):
            ans += dq[j]
        print(ans)
# O(N^3)
