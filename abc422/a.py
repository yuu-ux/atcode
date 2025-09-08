S = input().split('-')
i = int(S[0])
j = int(S[1])

if j < 8:
    j += 1
elif j == 8 and i < 8:
    i += 1
    j = 1
print(i, '-', j, sep='')

