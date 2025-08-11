from collections import Counter
S = Counter(input())
if S['A'] == 1 and S['B'] == 1 and S['C'] == 1:
    print('Yes')
else:
    print('No')
