def main():
    N, S = map(int, input().split())
    T = list(map(int, input().split()))

    ans = T[0]
    if ans >= (S + 0.5):
        print('No')
        return
    for i in range(1, N):
        ans = abs(T[i - 1] - T[i])
        if ans >= (S + 0.5):
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()
