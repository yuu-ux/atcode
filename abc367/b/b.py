# X = float(input())
# if X == int(X):
#     X = int(X)
# print(X)

X = float(input())
if X.is_integer():
    print(int(X))
else:
    print(X)
