from collections import Counter

A = Counter(map(int, input().split()))

if len(list(A)) != 2:
    print('No')
    exit()
for key, value in A.items():
    if value != 3 and value != 1 and value != 2:
        print('No')
        exit()
print('Yes')
