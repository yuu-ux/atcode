A = list(map(int, input().split()))

sorted_A = sorted(A)
if (sorted_A[0] * sorted_A[1]) == sorted_A[2]:
    print('Yes')
else:
    print('No')
