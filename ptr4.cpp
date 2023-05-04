#include <iostream>
using namespace std;

int main()
{
    class Solution
    {
    public:
        void printTriangle(int n)
        {
            // code here
            for (int i = 1; i <= n; i++)
            {
                for (int j = 1; j <= i; j++)
                {
                    cout << i << " ";
                }
                cout << endl;
            }
        }
    };
    Solution obj;
    obj.printTriangle(5);
}
/*
OUTPUT:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
*/

/*
class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, N + 1):
            for j in range(1, i + 1):
                 print(i, end=" ")
            print("")
*/