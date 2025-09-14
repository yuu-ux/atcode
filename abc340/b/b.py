Q = int(input())

A = []
for i in range(Q):
    x,y = map(int, input().split())
    if x == 1:
        A.append(y)
    elif x == 2:
        print(A[-y])
