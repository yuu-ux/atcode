S = input()
first = S[0]
second = S[1:]
if len(S) == 1 and first.isupper():
    print('Yes')
    exit()
if first.isupper() and second.islower():
    print('Yes')
else:
    print('No')
