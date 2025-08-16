# Y = int(input())
# if Y % 100 == 0 and Y % 400 != 0:
#         print(365)
# elif Y % 400 == 0:
#     print(366)
# elif Y % 4 != 0:
#     print(365)
# elif Y % 4 == 0 and Y % 100 != 0:
#     print(366)

from calendar import isleap
print(365+isleap(int(input())))
