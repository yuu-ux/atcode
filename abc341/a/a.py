N = int(input())

for i in range(N + N + 1):
    if i % 2 == 0:
        print(1, end='')
    else:
        print(0, end='')
print('')
