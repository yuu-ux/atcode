from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))
print(sum(v // 2 for v in A.values()))
# cnt = 0
# while sum(value >= 2 for _, value in A.items()) > 0:
#     for key, value in A.items():
#         if value >= 2:
#             cnt += 1
#             A[key] -= 2
# print(cnt)
