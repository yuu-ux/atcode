X, C = map(int, input().split())

for i in range(X, 0, -1):
    tessuryou = i * (C / 1000)
    if (i + tessuryou) <= X:
        print(int(i/1000)*1000)
        exit()
print(0)
