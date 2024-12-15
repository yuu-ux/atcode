#include <stdio.h>

void    print_binary(int N)
{
    int i;

    i = 10;

    while (i--)
    {
        if (((N >> i) & 1) == 1)
            printf("1");
        else
            printf("0");
    }
    printf("\n");
}

int main(void)
{
    int N;
    scanf("%d", &N);
    print_binary(N);
    return 0;
}
