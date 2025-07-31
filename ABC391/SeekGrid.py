N, M = map(int, input().split())

S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

def same_grid(S, T, i, j):
    M = len(T)
    for k in range(M):
        for l in range(M):
            if S[i + k][j + l] != T[k][l]:
                return False
    return True

def seek_grid(S, T):
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            if same_grid(S, T, i, j):
                return i+1, j+1

print(*(seek_grid(S, T)))

# N, M = map(int, input().split())
# S = [input() for _ in range(N)]
# T = [input() for _ in range(M)]
#
# for i in range(N - M + 1):
#     for col in range(len(S[i]) - len(T[0]) + 1):
#         matched = True
#         for j in range(M):
#             if col + len(T[j]) > len(S[i + j]) or S[i + j][col:col + len(T[j])] != T[j]:
#                 matched = False
#                 break
#         if matched:
#             print(i + 1, col + 1)
#             exit()
