# import copy
# N = int(input())
# A = list(map(int,input().split()))
# temp = copy.deepcopy(A)
#
# max_elem = max(temp)
# temp.remove(max_elem)
# max2_elem = max(temp)
#
# for i, v in enumerate(A):
#     if v == max2_elem:
#         print(i+1)
#         break

N = int(input())
A = list(map(int, input().split()))
print(A.index(sorted(A, reverse=True)[1])+1)
