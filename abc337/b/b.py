S = input()

if not S:
    print('Yes')
    exit()

if S == ''.join(sorted(S)):
    print('Yes')
else:
    print('No')
