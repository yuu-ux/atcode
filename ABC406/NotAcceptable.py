A, B, C, D = map(int, input().split())

# 12時10分 12時05分
if A > C:
    print('Yes')
elif A == C and B > D:
    print('Yes')
else:
    print('No')

