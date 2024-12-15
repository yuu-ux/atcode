#include <stdio.h>

int main(void)
{
    int L;
    int R;

    scanf("%d %d", &L, &R);
    if (L == 0 && R == 0)
        printf("Invalid\n");
    else if (L == 1 && R == 1)
        printf("Invalid\n");
    else if (L == 1 && R == 0)
        printf("Yes\n");
    else
        printf("No\n");
}
