A, B, C = map(int, input().split())

if A == B == C:
    print('Yes')
elif A + B == C:
    print('Yes')
elif A + C == B:
    print('Yes')
elif B + C == A:
    print('Yes')
else:
    print('No')
