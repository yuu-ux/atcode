N, L, R = map(int, input().split())

ans = [i for i in range(1, N+1)]
reverse_ans = sorted(ans[L-1:R], reverse=True)
print(*(ans[:L-1]+reverse_ans+ans[R:]))
