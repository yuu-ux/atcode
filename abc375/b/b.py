import math

N = int(input())

a,b = 0,0
res = 0
#(a,b) (c,d)
#(a-c)^2+(b-d)^2
for i in range(N):
    c,d = map(int, input().split())
    res += math.sqrt((a-c)**2+(b-d)**2)
    a = c
    b = d

res += math.sqrt((a-0)**2+(b-0)**2)
print(res)
