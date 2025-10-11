K, G, M = map(int, input().split())
grass = 0
mag = 0
for _ in range(K):
    if grass == G:
        grass = 0
    elif mag == 0:
        mag = M
    else:
        while mag != 0 and grass != G:
            mag -= 1
            grass += 1
print(grass, mag)
