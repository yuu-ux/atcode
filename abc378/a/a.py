from collections import Counter
A = Counter(map(int, input().split()))
res = 0
for key, value in A.items():
    if value >= 4:
        res += 2
    elif value >= 2:
        res += 1
print(res)


