#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int n;
    int m;
    scanf("%d %d", &n, &m);

    // flag管理する配列で初めはすべてfalseに設定する
    bool array[n];
    for (int i = 0; i < n; i++)
        array[i] = false;
    //受け取りと出力を同時にやる
    for (int i = 0; i < m; i++)
    {
        int a;
        char b;
        //入力を受け取る。aはインデックスとして使用したいため、デクリメントする
        scanf("%d %c", &a, &b);
        a--;
        // もしFかつ一回Yesを表示した家であればNoと出力。それ以外であればYesを出力
        if (b == 'F' || array[a])
            printf("No\n");
        else
        {
            array[a] = true;
            printf("Yes\n");
        }
    }
    return 0;
}
