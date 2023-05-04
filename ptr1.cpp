#include <string.h>
#include <iostream>
using namespace std;

class Solution
{
public:
    void printSquare(int n)
    {
        // code here
        for (int i = 0; i < n; i++)
        {
            string row = "";
            for (int j; j < n; j++)
            {
                row += "* ";
            }
            cout << row << endl;
        }
    }
};

/*
Input: 5

Output:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
*/

// #User function Template for python3

// class Solution:
//     def printSquare(self, N):
//         # Code here
//         for i in range(N):
//             row = ""
//             for j in range(N):
//                 row += '* '
//             print(row)