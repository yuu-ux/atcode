C_1 = list(map(int, input().split()))
C_2 = list(map(int, input().split()))

# x軸の右端、左端
x = max(0, min(C_1[3], C_2[3]) - max(C_1[0], C_2[0]))
# y軸の右端、左端
y = max(0, min(C_1[4], C_2[4]) - max(C_1[1], C_2[1]))
# z軸の右端、左端
z = max(0, min(C_1[5], C_2[5]) - max(C_1[2], C_2[2]))

if x * y * z > 0:
    print('Yes')
else:
    print('No')
