S, T = map(list, input().split())
for w in range(1, len(S)):
    for c in range(w):
        if S[c::w] == T:
            print('Yes')
            exit()
print('No')


# S, T = list(input().split())
# N = len(S)
#
# # 何文字区切りか決める
# for i in range(1, N):
#     # 区切った文字をループする
#     for j in range(0, i):
#         s = ''
#         # 区切った文字の k 番目を連結する
#         for k in range(j, N, i):
#             s += S[k]
#         if s == T:
#             print('Yes')
#             exit()
# print('No')

# x 文字ごとに区切るってx番目を抜き出す
# 抜き出した文字を ans に連結する
# if T in ans: print('Yes') else print('No')

