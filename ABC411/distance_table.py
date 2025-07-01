N = int(input())
D = list(map(int, input().split()))

for i in range(0, N-1):
    total = 0
    for j in range(i, N-1):
        total += D[j]
        print(total, end=' ')
    print('')
