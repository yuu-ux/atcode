A, B, C = map(int, input().split())

if B<C:
    if B <= A and A <= C:
        print('No')
    else:
        print('Yes')
else:
    if B <= A:
        print('No')
    elif A <= C:
        print('No')
    else:
        print('Yes')


# B <= A <= C → False
