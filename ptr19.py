class Solution:
    def printTriangle(self, N):
        # Code here
        star = N
        empty = 0
        for i in range(1, 2 * N + 1):
            for j in range(star):
                print("*", end="")
            for s in range(empty):
                print(" ", end="")
            for j in range(star):
                print("*", end="")
            if (i < N):
                empty += 2
                star -= 1
            elif (i == N):
                print("")
                continue
            else:
                empty -= 2
                star += 1
            print("")


Solution.printTriangle(None, 5)

'''

Input: 5

Output:
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

'''

'''
class Solution {
  public:
    void printTriangle(int n) {
        // code here
        int star = n;
        int empty = 0;
        for(int i = 1; i <= 2 * n; i++)
        {
            for(int j = 0; j < star; j++)
            {
                cout << "*";
            }
            for(int s = 0; s < empty; s++)
            {
                cout << " ";
            }
            for(int j = 0; j < star; j++)
            {
                cout << "*";
            }
            if (i < n)
            {
                empty += 2;
                star--;
            }
            else if (i == n)
            {
                cout << endl;
                continue;
            }
            else
            {
                empty -= 2;
                star++;
            }
            cout << endl;
        }
    }
};
'''