#include <stdio.h>

//次男を求める
int main(void)
{
    char S1;
    char S2;
    char S3;
    int A = 0;
    int B = 0;
    int C = 0;

    scanf("%c %c %c", &S1, &S2, &S3);
    if (S1 == '<')
        B += 1;
    else if (S1 == '>')
        A += 1;

    if (S2 == '<')
        C += 1;
    else if (S2 == '>')
        A += 1;

    if (S3 == '<')
        C += 1;
    else if (S3 == '>')
        B += 1;

    if (A == 1)
        printf("A\n");
    else if (B == 1)
        printf("B\n");
    else
        printf("C\n");
}
