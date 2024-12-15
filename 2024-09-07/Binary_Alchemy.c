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
    for (int i = 1; i <= N; i++)
    {
        A[i] = (int *)calloc(sizeof(int), i);
        for (int j = 1; j <= i; j++)
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
            res = A[res][j];
        else
            res = A[j][res];
    }
    printf("%d\n", res);
}
