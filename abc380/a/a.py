from collections import Counter
N = Counter(input())

if N['1'] != 1 or N['2'] != 2 or N['3'] != 3:
    print('No')
    exit()
print('Yes')
