from collections import Counter

N = int(input())
A = list(map(int, input().split()))

Ai_plus_i = Counter(A[i] + i for i in range(N))
print(sum(Ai_plus_i[j-A[j]] for j in range(N)))


# from collections import defaultdict
#
# N = int(input())
# A = list(map(int, input().split()))
#
# cnt = 0
# counter = defaultdict(int)
# for i in range(N):
#     a = A[i]
#     cnt += counter[i - a]
#     counter[i + a] += 1
#     print(counter)
# print(cnt)

# cnt = 0
# for i in range(N):
#     if A[i] >= N:
#         continue
#     for j in range(A[i], N):
#         if j - i == A[i] + A[j]:
#             cnt += 1
# print(cnt)

# 20 億
# 20 万
# 400 億
