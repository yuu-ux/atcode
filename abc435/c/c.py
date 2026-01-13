N = int(input())
A = list(map(int, input().split()))

r = 0
i = 0
while i <= r and i < N:
    r = max(r, i + A[i] - 1)
    i += 1

print(min(N, r + 1))

# i 以上 i + Ai 未満のドミノが倒れる
# 1, 初めのドミノの数が1以上であればドミノを倒す
# 2, 最後に倒れたドミノを確認し、1でなければさらにドミノを倒す
# 3, 最後に倒したドミノが1になるまで繰り返す

# res = 0
# last_domino = 0
# index = 0
# while last_domino != 1 and index < N:
#     if A[index] == 1:
#         res += 1
#         break
#     res += A[index]
#     down = A[index]
#     index = down-1
#     last_domino = A[index]
# if res > N:
#     res = N
# print(res)


