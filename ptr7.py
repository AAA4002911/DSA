class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            for j in range(N - i - 1):
                print(" ", end="")
            for k in range(2 * i + 1):
                print("*", end="")
            print("")

Solution.printTriangle(None, 5)


'''
Input: 5

Output:
    *
   ***  
  *****
 *******
*********
'''


'''
class Solution {
  public:
    void printTriangle(int n) {
        // code here
        for (int i = 0 ; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                cout << " ";
            }
            for (int k = 0; k < 2 * i + 1; k++) {
                cout << "*";
            }
            cout << endl;
        }
    }
};
'''