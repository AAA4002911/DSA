#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
    class Solution
    {
    public:
        void printDiamond(int n)
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n - i - 1; j++)
                {
                    cout << " ";
                }
                for (int k = 0; k < i + 1; k++)
                {
                    cout << "* ";
                }
                cout << endl;
            }

            for (int i = n; i > 0; i--)
            {
                for (int j = 0; j < n - i; j++)
                {
                    cout << " ";
                }
                for (int k = i; k > 0; k--)
                {
                    cout << "* ";
                }
                cout << endl;
            }
        }
    };

    Solution obj;
    obj.printDiamond(5);
}


/*

    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *

*/


/*
class Solution:
    def printDiamond(self, N):
        for i in range(N):
            for j in range(N - i - 1):
                print(" ", end="")
            for k in range(i + 1):
                print("* ", end="")
            print("")

        for i in range(N, 0, -1):
			for j in range(N - i):
				print("", end=" ")
			for k in range(i, 0, -1):
				print("* ", end="")
			print("")
*/