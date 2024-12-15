#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N;
    int **A;
    int res;

    if (scanf("%d", &N) == -1)
        return 1;
    A = (int **)malloc(sizeof(int *) * N);
    // 入力を受け取る
    for (int i = 0; i < N; i++)
    {
        A[i] = (int *)calloc(i+1, sizeof(int));
        for (int j = 0; j <= i; j++)
        {
            if (scanf("%d", &A[i][j]) == -1)
                return 1;
        }
    }
    res = 1;

    // 元素を合成する
    for (int j = 1; j <= N; j++)
    {
        if (res >= j)
            res = A[res-1][j-1];
        else
            res = A[j-1][res-1];
    }
    printf("%d\n", res);
}
