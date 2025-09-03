N = int(input())
A = list(map(int, input().split()))

B = {a:i for i,a in enumerate(A)}

ans = []
for i in range(N):
    if A[i] == i+1:
        continue
    j = B[i+1]
    ans.append((i+1, j+1))
    A[i], A[j] = A[j], A[i]
    B[A[j]] = j
    B[A[i]] = i

print(len(ans))
for a in ans:
    print(*a)

# N = int(input())
# A = [0] + list(map(int, input().split()))
#
# B = [0] * (N + 1)
# for i in range(1, N+1):
#     B[A[i]] = i
#
# ans = []
# for i in range(1, N+1):
#     if A[i] == i:
#         continue
#     j = B[i]
#     ans.append((i, j))
#     A[i], A[j] = A[j], A[i]
#     B[A[i]] = i
#     B[A[j]] = j
#
# print(len(ans))
# for a in ans:
#     print(*a)
