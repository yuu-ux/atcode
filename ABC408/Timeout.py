def main():
    N, S = map(int, input().split())
    T = list(map(int, input().split()))

    ans = T[0]
    for i in range(1, N):
        print(ans)
        if ans >= (S + 0.5):
            print('Yes')
            return
        ans = abs(T[i - 1] - T[i])
    print('No')

if __name__ == '__main__':
    main()

