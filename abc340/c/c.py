# from functools import cache
# N = int(input())
#
# @cache
# def total_sum(n):
#     if n <= 1:
#         return 0
#     a = n // 2
#     b = n - a
#     return n + total_sum(a) + total_sum(b)
#
# print(total_sum(N))


N = int(input())
memo = {}
def total_sum(n):
    if n in memo:
        return memo[n]
    if n == 1:
        ret = 0
    else:
        ret = n + total_sum(n // 2) + total_sum((n + 1) // 2)
    memo[n] = ret
    return ret
print(total_sum(N))
