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
                for (int s = 1; s <= n - i; s++)
                {
                    cout << " ";
                }
                for (int j = 1; j <= i; j++)
                {
                    cout << letter[j - 1];
                }
                for (int k = i - 1; k >= 1; k--)
                {
                    cout << letter[k - 1];
                }
                cout << endl;
            }
        }
    };

    Solution ptr17;
    ptr17.printTriangle(4);
}

/*
Input: 4
Output:
   A
  ABA
 ABCBA
ABCDCBA
*/

// letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
// for i in range(1, N + 1):
//     for s in range(1, N - i + 1):
//         print(" ", end="")
//     for j in range(1, i + 1):
//         print(letter[j - 1], end="")
//     for k in range(i - 1, 0, -1):
//         print(letter[k - 1], end="")
//     print("")