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
            for (int i = n; i > 0; i--)
            {
                for (int j = 1; j <= i; j++)
                {
                    cout << letter[j - 1];
                }
                cout << endl;
            }
        }
    };

    Solution ptr15;
    ptr15.printTriangle(5);
}

/*
Input: 5

Output:
ABCDE
ABCD
ABC
AB
A
*/

// letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
// for row in range(N, 0, -1):
//     for i in range(1, row + 1):
//         print(letter[i - 1], end="")
//     print("")