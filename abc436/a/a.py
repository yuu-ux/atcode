N = int(input())
S = list(input())

while len(S) != N:
    S.insert(0, 'o')
print(''.join(S))
