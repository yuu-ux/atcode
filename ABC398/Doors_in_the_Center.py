N = int(input())
if N % 2 == 0:
    c = (N - 2) // 2
    print('-' * c + '='*2 + '-'*c)
else:
    c = (N-1)//2
    print('-' * c+ '=' + '-' * c)
