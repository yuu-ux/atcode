H = int(input())

i = 0
grow = 0
while grow <= H:
    grow += pow(2, i)
    i += 1

print(i)
