import string

S = input()
T = input()
alpha = {ascii: 0 for ascii in string.ascii_letters}

for t in T:
    alpha[t]  = 1

index = []
for i, s in enumerate(S):
    if s.isupper() and i >= 2:
        index.append(i)

res = 'Yes'
for i in index:
    if alpha[S[i - 1]] == 1:
        res = 'Yes'
    else:
        res = 'No'
        break
print(res)
