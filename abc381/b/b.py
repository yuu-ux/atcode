from collections import Counter
S = list(input())

s_len = len(S)
if s_len % 2 != 0:
    print('No')
    exit()

for i in range(1, s_len//2+1):
    if S[2*i-1] != S[2*i - 2]:
        print('No')
        exit()

counter_s = Counter(S)
for _, value in counter_s.items():
    if value != 2:
        print('No')
        exit()

print('Yes')
