# from collections import defaultdict
#
# N = int(input())
# P = list(map(lambda x: -int(x), input().split()))
# sorted_P = sorted(P)
# D = defaultdict(int)
# for i, v in enumerate(sorted_P):
#     if D[v] == 0:
#         D[v] = i + 1
#     else:
#         continue
# print(*map(lambda v: D[v], P), sep='\n')


from collections import defaultdict
N = int(input())
P = list(map(int, input().split()))
dict_P = defaultdict(int)
for value, key in enumerate(sorted(P, reverse=True), 1):
    if dict_P[key] == 0:
        dict_P[key] = value
for p in P:
    print(dict_P[p])

# from collections import Counter
#
# N = int(input())
# P = list(map(int, input().split()))
# counter_P = Counter(P).items()
# counter_P = sorted(counter_P, key=lambda x: x[0], reverse=True)
# r = 1
# print(counter_P)
# for index, value in enumerate(counter_P):
#     print(index, value)
