N, M = map(int, input().split())
A =  list(map(int, input().split()))
B = list(map(int, input().split()))

AB = []
AB.extend(A)
AB.extend(B)
AB.sort()
for i in range(N+M-1):
    if AB[i] in A and AB[i+1] in A:
        print('Yes')
        exit()
print('No')

