H, B = map(int, input().split())

if H <= B:
    print(0)
    exit()
print(H - B)
