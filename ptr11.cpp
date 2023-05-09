#include <iostream>
using namespace std;

int main()
{
    class Solution
    {
    public:
        void printTriangle(int n)
        {
            for (int row = 1; row <= n; row++)
            {
                int ptr = row % 2 ? 1 : 0;
                for (int i = 1; i <= row; i++)
                {
                    cout << ptr << " ";
                    ptr = ptr == 1 ? 0 : 1;
                }
                cout << endl;
            }
        }
    };

    Solution ptr11;
    ptr11.printTriangle(5);
}

/*
class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):
            ptr = 1 if i % 2 else 0
            for j in range(1, i + 1):
                print(ptr, end=" ")
                ptr = 1 if ptr == 0 else 0
            print("")
*/