S = list(input().split())

if S[0] == 'sick' and S[1] == 'sick':
    print(1)
elif S[0] == 'sick':
    print(2)
elif S[1] == 'sick':
    print(3)
else:
    print(4)

