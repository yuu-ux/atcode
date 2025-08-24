A, B = map(int, input().split())

if A == 1 and B == 2 or B == 1 and A == 2:
    print(3)
elif A == 2 and B == 3 or B == 2 and A == 3:
    print(1)
elif A == 3 and B == 1 or B == 3 and A == 1:
    print(2)
else:
    print(-1)
