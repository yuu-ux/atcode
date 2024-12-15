using namespace std;
#include <iostream>
#include <vector>
#include <utility>

int main(void)
{
    int N;
    int X;
    int i;
    int time;
    vector<pair<int, int>> T;

    X = 0;
    i = 0;
    time = 0;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int x, y;
        cin >> x >> y;
        T.emplace_back(x, y);
    }

    while (i < T.size())
    {
        if (X != 0)
            X -= 1;
        if (time == T[i].first)
        {
            X += T[i].second;
            i++;
        }
        time++;
    }
    cout << X << endl;
}
