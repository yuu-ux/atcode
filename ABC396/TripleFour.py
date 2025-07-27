N = int(input())
A = list(map(int, input().split()))

for i in range(1, N - 1):
    if A[i - 1] == A[i] == A[i + 1]:
        print('Yes')
        exit()
print('No')
