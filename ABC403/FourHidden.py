import string

T = input()
U = input()

includes = [i for i in range(len(T)) if T[i] == '?']
alphabets = list(string.ascii_lowercase)
for a in alphabets:
    for b in alphabets:
        for c in alphabets:
            for d in alphabets:
                S = list(T)
                S[includes[0]] = a
                S[includes[1]] = b
                S[includes[2]] = c
                S[includes[3]] = d
                S = ''.join(S)
                if U in S:
                    print('Yes')
                    exit()
print('No')
