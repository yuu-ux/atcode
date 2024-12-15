#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N;
    int X;
    int *A;
    int flag;

    flag = 0;
    scanf("%d %d", &N, &X);
    A = (int *)malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }

    for (int i = 0; i < N; i++)
    {
        if (X == A[i])
            flag = 1;
    }
    if (flag)
        printf("Yes\n");
    else
        printf("No\n");
    free(A);
}
