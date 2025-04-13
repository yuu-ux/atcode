using namespace std;
#include <iostream>

int main(void)
{
    int A, B, C, D, count;
    cin >> A, B, C, D;
    count = 1;
    if (A == B)
        count++;
    if (A == C)
        count++;
    if (A == D)
        count++;
    if (count == 2 || count == 3)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}
