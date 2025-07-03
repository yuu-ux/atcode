N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
for x in range(N, 0, -1):
    if A[x - 1] >= x:
        print(x)
        exit()
print(0)
