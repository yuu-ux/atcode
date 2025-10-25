import copy
N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    temp = copy.deepcopy(A)
    temp.pop(i)
    if sum(temp) == M:
        print('Yes')
        break
else:
    print('No')
