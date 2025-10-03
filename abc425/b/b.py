N = int(input())
A = list(map(int, input().split()))

# 存在するものをカウントする
table = {i: 0 for i in range(1,N+1)}
for a in A:
    if a != -1:
        table[a] = 1

# 存在しないものリスト
not_exist = []
for i, v in table.items():
    if v == 0:
        not_exist.append(i)

# 数列pを作る
ans = []
for a in A:
    if a == -1:
        ans.append(not_exist.pop(0))
    else:
        ans.append(a)

# 判定
if not not_exist:
    print('Yes')
    print(*ans)
else:
    print('No')

# N = int(input())
# A = list(map(int, input().split()))
# table = set(range(1, N+1))
# not_exist = list(table - set(A))
#
# ans = []
# if len(not_exist) == A.count(-1):
#     print('Yes')
#     for i in range(N):
#         if A[i] == -1:
#             ans.append(not_exist.pop(0))
#         else:
#             ans.append(A[i])
#     print(*ans)
# else:
#     print('No')
