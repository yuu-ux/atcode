import sys
input = sys.stdin.read

def main():
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        N = int(data[index])
        index += 1
        S = list(map(int, data[index:index + N]))
        index += N

        # 貪欲に逆からたどる
        selected = [N - 1]  # 最後のドミノN（index N-1）からスタート

        for i in range(N - 2, -1, -1):  # 後ろから前へ
            if S[i] * 2 >= S[selected[-1]]:
                selected.append(i)

        # 最後に、ドミノ1（index 0）が含まれていないと不成立
        if selected[-1] != 0:
            results.append("-1")
        else:
            results.append(str(len(selected)))

    print("\n".join(results))

main()
