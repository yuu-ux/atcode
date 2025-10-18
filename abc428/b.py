from collections import defaultdict

N, K = map(int, input().split())
S = list(input())

count = defaultdict(int)
for i in range(N-K+1):
    key = ''.join(S[i:K+i])
    count[key] += 1
sorted_dict = sorted(count.items(), key=lambda x:x[1], reverse=True)
_max = 0
for key, value in sorted_dict:
    _max = value
    print(_max)
    break
ans = []
for key, value in sorted_dict:
    if _max == value:
        ans.append(key)
print(*sorted(ans))
