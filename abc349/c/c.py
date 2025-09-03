S = input().upper()
T = list( input() )

s_len = len(S)
for i in range(s_len):
    if S[i] == T[0]:
        T.pop(0)
    if not T:
        print('Yes')
        exit()
if len(T) == 1 and T[0] == 'X':
    print('Yes')
else:
    print('No')
