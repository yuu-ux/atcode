X = int(input())

# N = 1
# res = 1
# while res != X:
#     N += 1
#     res *= N
# print(N)

def recursive(x, n, res):
    if res == x:
        return n
    return recursive(x, n + 1, res * (n + 1))
print(recursive(X, 1, 1))
