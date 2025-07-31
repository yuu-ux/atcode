# N, M = map(int, input().split())
#
# S = [input() for _ in range(N)]
# T = [input() for _ in range(M)]
#
# for i in range(N - M + 1):
#     matched = True
#     for j in range(N - M + 1):
#         if S[i][j]
#             break
#         if matched:
#             print(i + 1, index + 1)
#             exit()

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for i in range(N - M + 1):
    for col in range(len(S[i]) - len(T[0]) + 1):
        matched = True
        for j in range(M):
            if col + len(T[j]) > len(S[i + j]) or S[i + j][col:col + len(T[j])] != T[j]:
                matched = False
                break
        if matched:
            print(i + 1, col + 1)
            exit()
