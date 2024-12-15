using namespace std;
#include <iostream>
#include <vector>

int main()
{
    vector<long long> A(4);
    long long cnt;
    long long temp;
    long long flg;

    flg = 1;
    cnt = 0;
    for (int i = 0; i < 4; i++)
        cin >> A[i];
    for (int i = 0; i < 4; i++)
    {
        for (int j = i+1; j < 3; j++)
        {
            if (A[i] == A[j])
                flg = 0;
            else
                flg = 1;
        }
    }
    cout << cnt << endl;
}
