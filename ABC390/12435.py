A = list(map(int, input().split()))

cnt = 0
for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
            cnt += 1

if cnt == 1:
    print('Yes')
else:
    print('No')
