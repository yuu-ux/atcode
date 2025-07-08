def rotate_90(S, N):
    rotated_S = [[''] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated_S[j][N - (i + 1)] = S[i][j]
    return rotated_S

def count_false(T, S, N):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                cnt += 1
    return cnt

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        S.append(list(input()))
    for _ in range(N):
        T.append(list(input()))

    # 0, 90, 180, 270 度で一番一致する個数が多い角度を求める
    # current_cnt = count_false(T, S, N)
    ans = count_false(T, S, N)
    rotated_S = S
    ans_array = S
    current_ans = 0
    for i in range(4):
        current_ans = count_false(T, rotated_S, N) + i
        if ans > current_ans:
            ans = current_ans
        rotated_S = rotate_90(rotated_S, N)

    print(ans)

if __name__ == '__main__':
    main()
