#include <iostream>
#include <string.h>

using namespace std;
int main()
{
    class Solution
    {
    public:
        void printTriangle(int n)
        {
            string letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            for (int i = 1; i <= n; i++)
            {
                for (int j = 1; j <= i; j++)
                {
                    cout << letter[i - 1];
                }
                cout << endl;
            }
        }
    };

    Solution ptr16;
    ptr16.printTriangle(5);
}

/*
Input: 5

Output:
A
BB
CCC
DDDD
EEEEE
*/

// letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
// for row in range(1, N + 1):
//     for i in range(1, row + 1):
//         print(letter[row - 1], end="")
//     print("")