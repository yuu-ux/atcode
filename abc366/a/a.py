N, T, A = map(int, input().split())

nokori = abs(N - (T + A))
hyousa = abs(T - A)
if nokori <= hyousa:
    print('Yes')
else:
    print('No')
