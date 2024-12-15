using namespace std;
#include <map>
#include <vector>
#include <iostream>

int main()
{
    long long n;
    cin >> n;
    vector<long long> input(n);
    map<long long, long long> map;

    for (int i = 0; i < n; i++)
        cin >> input[i];
    for (int i = 0; i < n; i++)
    {
        if (map[input[i]] == 0)
        {
            cout << -1 << " ";
        }
        else
        {
            cout << map[input[i]] << " ";
        }
        map[input[i]] = i + 1;
    }
    cout << endl;
}
