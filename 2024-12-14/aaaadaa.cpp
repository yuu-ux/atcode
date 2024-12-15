using namespace std;
#include <iostream>

int main(void)
{
    int N;
    char c1;
    char c2;
    string S;
    cin >> N >> c1 >> c2;
    cin >> S;
    for (int i = 0; i < N; i++)
    {
        if (S[i] != c1)
            S[i] = c2;
    }
    cout << S << endl;
}
