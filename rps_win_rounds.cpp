#include <bits/stdc++.h>
#include <fstream>
using namespace std;

mt19937 gen(random_device{}());
uniform_int_distribution<> distr;

short rps(unsigned short p, unsigned short q, unsigned short r)
{
    distr.param(uniform_int_distribution<>::param_type(1, p + q + r));
    int randnum = distr(gen);
    if (randnum <= p) return 2;
    else if (randnum <= p + q) return 1;
    else return 0;
}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    unsigned short p, q, r;
    long n, a, b, x = 0, y = 0, rc = 0, src = 0;
    int xwc = 0, ywc = 0, tc = 100000;

    // cin >> p >> q >> r;
    // cin >> n >> a >> b;
    p = 1, q = 1, r = 1, a = 2, b = 1;

    ofstream file1("round_data_100_1000_10.csv", ios::app);  // Open a file to append src values

    for (n = 100; n <= 1000; n += 10){

    // cin >> n;

    for (long long i = 0; i < tc; i++)
    {
        while (1)
        {
            int game_result = rps(p, q, r);
            if (game_result == 2) // x wins
            {
                x += a;
                y > b ? y -= b : y = 0;
            }
            else if (game_result == 0) // y wins
            {
                x > b ? x -= b : x = 0;
                y += a;
            }
            
            src++;
            rc++;
        
            if (x >= n || y >= n)
            {
                file1 << n << "," << src << "\n";  // Write src to file before resetting
                xwc += x >= n ? 1 : 0;
                ywc += y >= n ? 1 : 0;
                x = 0; y = 0; src = 0;
                break;
            }
        }
    }

    // cout << xwc << " " << ywc << " " << (long double) rc / tc;

    }
    file1.close();  // Close the file
    return 0;
}
