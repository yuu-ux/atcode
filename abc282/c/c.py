N = int(input())
S = list(input())

flg_around = False
for i in range(N):
    if flg_around == False and S[i] == '\"':
        flg_around = True
    elif flg_around == True and S[i] == '\"':
        flg_around = False
    if flg_around == False and S[i] == ',':
        S[i] = '.'
print(''.join(S))
