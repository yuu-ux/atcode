from collections import Counter
S = input()
counter_s = Counter(S)
sort_s = sorted(counter_s.items(), key=lambda x: (-x[1], x[0]))
print(sort_s[0][0])
