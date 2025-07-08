from collections import deque
Q = int(input())
# A = []
A = deque()
# (c, x) のリストを作る
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, c, x = query
        A.append([c, x])
    elif query[0] == 2:
        k = query[1]
        ans = 0
        while k > 0:
            c, x = A[0]
            if c <= k:
                k -= c
                ans += c * x
                # del A[0]
                A.popleft()
            else:
                ans += k * x
                A[0][0] -= k
                # k = 0
                break
        print(ans)
