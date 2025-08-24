S = list(input())
s_len = len(S)
zero = 0
i = 0
while i < s_len:
    if i < s_len-1 and S[i] == '0' and S[i+1] == '0':
        zero += 1
        i += 2
        continue
    i += 1
print(s_len - zero)
