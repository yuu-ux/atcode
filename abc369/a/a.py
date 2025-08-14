A, B = map(int, input().split())
if A == B:
    print(1)
elif abs(A - B) % 2 == 0:
    print(3)
else:
    print(2)

# ans =0
# temp = abs(A-B)
# i = min(A, B)-temp
# while  i <= max(A, B)+temp:
#     if B-A == i-B:
#         ans+=1
#     i+=1
# print(ans)

# ABx
# pqr
# q-p == r-q
# B-A == x-B
# 5-7 == 3-5
# 2==2
