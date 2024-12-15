using namespace std;
#include <iostream>

bool is_div1(int R)
{
    return (R >= 1600 && R <= 2799);
}

bool is_div2(int R)
{
    return (R >= 1200 && R <= 2399);
}

int main(void)
{
    int N;
    int R;
    short D;
    int A;
    cin >> N >> R;
    for (int i = 0; i < N; i++)
    {
        cin >> D >> A;
        if (D == 1)
        {
            if (is_div1(R))
                R += A;
        }
        else if (D == 2)
        {
            if (is_div2(R))
                R += A;
        }
    }
    cout << R << endl;
}
