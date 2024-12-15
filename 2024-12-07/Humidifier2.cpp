using namespace std;
#include <iostream>
#include <vector>

int main(void)
{
    int H;
    int W;
    int D;
    cin >> H >> W >> D;

    vector<string> grid(H);

    for (int i = 0; i < H; i++)
    {
        cin >> grid[i];
    }
    for (int i = 0; i < grid.size(); i++)
    {
        cout << grid[i] << endl;
    }
}
