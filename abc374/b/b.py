# S = input()
# T = input()
#
# s_len = len(S)
# t_len = len(T)
# length = 0
# if s_len > t_len:
#     length = t_len
# else:
#     length = s_len
# for i in range(length):
#     if S[i] != T[i]:
#         print(i+1)
#         exit()
# if s_len > t_len:
#     print(t_len+1)
# elif t_len > s_len:
#     print(s_len+1)
# else:
#     print(0)

S = input()
T = input()

s_len = len(S)
t_len = len(T)
for i in range(min(s_len, t_len)):
    if S[i] != T[i]:
        print(i+1)
        exit()
if s_len != t_len:
    print(min(s_len, t_len)+1)
else:
    print(0)
