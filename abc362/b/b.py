A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

AB = pow(A[0] - B[0],2) + pow(A[1] - B[1],2)
BC = pow(B[0] - C[0],2) + pow(B[1] - C[1],2)
CA = pow(C[0] - A[0],2) + pow(C[1] - A[1],2)


if AB + BC == CA or BC + CA == AB or CA + AB == BC:
    print('Yes')
else:
    print('No')
