N = int(input())
S = [input() for _ in range(N)]
max_length = max(map(len, S))
for i in range(max_length):
    row = []
    for j in range(N-1, -1, -1):
        if i < len(S[j]):
            row.append(S[j][i])
        else:
            row.append('*')
    print(''.join(row).rstrip('*'),sep='')

# j が縦軸
    # 単語の数
# i が横軸
    # 文字数が他の文字より短い場合超える可能性がある
