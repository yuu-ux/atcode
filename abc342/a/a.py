from collections import Counter
S = input()
counter_s = Counter(S)
for k, v in counter_s.items():
    if v == 1:
        print(S.index(k)+1)
