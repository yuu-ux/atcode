S = list(input())

length = len(S)
cnt = 0

for i in range(length):
    if S[i] == 'A':
        index_A = i
        j = i
        while j < length:
            if S[j] == 'B':
                index_C = j + (j - index_A)
                if index_C < length:
                    if S[index_C] == 'C':
                        cnt += 1
                else:
                    break
            j += 1
print(cnt)

# python はネストが深くなると読みにくいため、例外を弾いていくような書き方をする
# += 演算子は遅いため、なるべく使わない。(while をなるべく使わない)
# for i in range(length):
#     if S[i] != 'A':
#         continue
#     for j in range(i + 1, length):
#         if S[j] != 'B':
#             continue
#         k = 2 * j - i
#         if k >= length:
#             continue
#         if S[k] != 'C':
#             continue
#         cnt += 1
