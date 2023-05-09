#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
    class Solution
    {
    public:
        void printTriangle(int n)
        {
            int k = 1;
            for (int i = 1; i < 2 * n; i++)
            {
                int limit = i;
                if (i > n)
                {
                    limit = n - k;
                    k++;
                }
                for (int j = 1; j <= limit; j++)
                {
                    cout << "*"
                         << " ";
                }
                cout << endl;
            }
        }
    };

    Solution obj;
    obj.printTriangle(5);
}

/*
Input: 5

Output:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
*/

/*
class Solution:
    def printTriangle(self, N):
        k = 1;
        for  i in range(1, 2 * N):
            limit = i
            if (i > N):
                limit = N - k;
                k += 1
            for j in range (limit):
                print("*", end=" ")
            print("")
*/