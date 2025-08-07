#
# def check_flore(i, j, D, S, H, W):
#     cnt = 0
#     for k in range(H):
#         for l in range(W):
#             if abs(i - k) + abs(j - l) <= D and S[k][l] == '.':
#                 cnt += 1
#     return cnt
#
# res = 0
# temp = 0
# for i in range(H):
#     for j in range(W):
#         for k in range(H):
#             for l in range(W):
#                 if S[i][j] == '.' and S[k][l] == '.':
#                     temp += check_flore(i, j, D, S, H, W)
#                     temp += check_flore(k, l, D, S, H, W)
#                 if temp > res:
#                     res = temp
# print(res)

from itertools import product
H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = 0
for a, b, c, d in product(range(H), range(W), repeat=2):
    if S[a][b] != '.' or S[c][d] != '.' or (a == c and b == d):
        continue
    cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] != '.':
                continue
            if abs(a - i) + abs(b - j) <= D or abs(c - i) + abs(d - j) <= D:
                cnt += 1
    ans = max(ans, cnt)

print(ans)
