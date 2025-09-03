from collections import Counter

S = Counter(input())
ans = {}
for v in S.values():
    if v in ans:
        ans[v] += 1
    else:
        ans[v] = 1

for k, v in ans.items():
    if 0 != v and 2 != v:
        print('No')
        exit()
print('Yes')
