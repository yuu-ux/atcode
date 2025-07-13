def main():
    N = int(input())
    inputs = [input() for _ in range(N)]
    limit = 0
    ans = ''
    for i in range(N):
        c, _l = inputs[i].split()
        l = int(_l)
        limit += l
        if limit > 100:
            print('Too Long')
            return
        ans += c * l
    print(ans)

if __name__ == '__main__':
    main()
