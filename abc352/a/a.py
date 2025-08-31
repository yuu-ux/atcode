N, X, Y, Z = map(int, input().split())

i = min(X, Y)
while i <= max(X, Y):
    if i == Z:
        print('Yes')
        exit()
    i += 1
print('No')
