using namespace std;
#include <iostream>
#include <vector>
#include <algorithm>

int main(void)
{
    int n;
    n = 5;
    vector<long long> A(n);
    vector<pair<long, string>> P;

    for (int i = 0; i < n; i++)
        cin >> A[i];
    for (int bit = 1; bit < (1 << 5); bit++)
    {
        string s = "";
        long long sum = 0;
        for (int i = 0; i < n; i++)
        {
            if ((bit >> i) & 1)
            {
                s += 'A' + i;
                sum += A[i];
            }
        }
        P.push_back(make_pair(sum, s));
    }
    sort(P.begin(), P.end(), [](const pair<long long, string> &l, const pair<long long, string> &r) {
        if (l.first != r.first)
            return l.first > r.first;
        return l.second < r.second;
            });
    for (int i = 0; i < 31; i++)
    {
        cout <<  P[i].second << endl;
    }
}

//2^5-1 の 31 通り
