N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
if A == sorted_A:
    set_A = set(A)
    if len(set_A) == len(A):
        print('Yes')
    else:
        print('No')
else:
    print('No')
