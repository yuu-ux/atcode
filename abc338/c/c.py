# N = int(input())
# Q = list(map(int, input().split()))
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# INF = 10**18
#
# ans = 0
# for x in range(max(Q) +1):
#     y = INF
#     for i in range(N):
#         if Q[i] < A[i] * x:
#             y = -INF
#         elif B[i] > 0:
#             y = min(y, (Q[i] - A[i] * x) // B[i])
#     ans = max(ans, x + y)
# print(ans)

N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# a の候補を列挙する
max_a = min((Q[i] // A[i] for i in range(N) if A[i] > 0), default=0)

# b を確定させる
res = []
ans = -1
# 0からaの候補分全て回したい
for a in range(max_a+1):
    # 可能フラグ
    feasible = True
    caps = []

    for i in range(N):
        # この時点で a が作れないからbreak
        rem = Q[i] - A[i] * a
        if  rem < 0:
            feasible = False
            break
        # 0 徐算にならないように
        if B[i] > 0:
            # これがbの個数の選択肢となる
            caps.append(rem // B[i])
    if not feasible:
        continue
    b = min(caps) if caps else 0

    # ans を更新し続けて一番大きな数が答えとなる
    s = a + b
    if s > ans:
        ans = s
        best = (a, b)
print(ans)
