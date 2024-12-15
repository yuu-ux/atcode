#include <stdio.h>

int main(void)
{
    int N;
    int K;
    int count;

    count = 0;
    scanf("%d %d", &N, &K);
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            for (int k = 1; k <= N; k++)
            {
                if ((i + j + k) == K)
                    count++;
            }
        }
    }
    printf("%d\n", count);
    return 0;
}
