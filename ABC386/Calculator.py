S = list(input())

cnt = 0
i = 0
while i < len(S):
    if i+1 < len(S) and S[i] == '0' and S[i + 1] == '0':
        i += 2
    else:
        i += 1
    cnt += 1
print(cnt)

# S = list(input())
# cnt = 0
# while S:
#     cnt += 1
#     if S.pop() == '0' and S and S[-1] == '0':
#         S.pop()
# print(cnt)
