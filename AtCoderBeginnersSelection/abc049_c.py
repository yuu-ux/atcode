S = input()

while S:
    if S.endswith('dreamer'):
        S = S.removesuffix('dreamer')
    elif S.endswith('dream'):
        S = S.removesuffix('dream')
    elif S.endswith('eraser'):
        S = S.removesuffix('eraser')
    elif S.endswith('erase'):
        S = S.removesuffix('erase')
    else:
        print('NO')
        exit()
print('YES')

# dream dreamer erase eraser
