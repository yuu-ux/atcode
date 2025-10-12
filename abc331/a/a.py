M, D = map(int, input().split())
y, m, d = map(int, input().split())

# next_day = d+1
# if next_day < D:
#     print(y,m,next_day)
#     exit()
# next_day -= D
# next_month = m+1
# if next_month < M:
#     print(y,next_month,next_day)
#     exit()
# next_month -= M
# print(y+1, next_month, next_day)

next_day = d % D + 1
if d < next_day:
    print(y,m,next_day)
    exit()
next_month = m % M + 1
if m < next_month:
    print(y,next_month,next_day)
    exit()
print(y+1,next_month,next_day)
