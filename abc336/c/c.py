N = int(input())

def base_n(num_10,n):
    if num_10 == 0:
        return 0
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

print(base_n(N-1, 5) * 2)
