class Solution:
    def printTriangle(self, N):
        # Code here
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for row in range(1, N + 1):
            for i in range(1, row + 1):
                print(letter[i - 1], end="")
            print("")
    
Solution.printTriangle(None, 5)


'''
Input: 5

Output:
A
AB
ABC
ABCD
ABCDE
'''

'''
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
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= i; j++) {
                    cout << letter[j - 1];
                }
                cout << endl;
            }
        }
    };

    Solution ptr15;
    ptr15.printTriangle(1);
}
'''