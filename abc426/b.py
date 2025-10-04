S = list(input())

set_s = set(S)
list_s = list(set_s)
if S.count(list_s[0])  > S.count(list_s[1]):
    print(list_s[1])
else:
    print(list_s[0])
