def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    for _ in range(N):
        if len(set(A)) != M:
            print(cnt)
            return
        A.pop(-1)
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
