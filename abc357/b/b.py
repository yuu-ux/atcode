S = input()

lower_cnt = 0
upper_cnt = 0
for s in S:
    if s.islower():
        lower_cnt += 1
    elif s.isupper():
        upper_cnt += 1
if lower_cnt < upper_cnt:
    print(S.upper())
else:
    print(S.lower())
