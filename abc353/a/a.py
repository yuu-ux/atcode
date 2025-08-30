N = int(input())
A = list(map(int, input().split()))

for i in range(1, N):
    if A[0] < A[i]:
        print(i+1)
        exit()
print(-1)
