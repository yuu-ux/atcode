import math

A, B = map(int, input().split())
res = A / B
ceil = math.ceil(res)
floor = math.floor(res)
_ceil = abs(res - math.ceil(res))
_floor = abs(res - math.floor(res))

if _ceil > _floor:
    print(floor)
else:
    print(ceil)
