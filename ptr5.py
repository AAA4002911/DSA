class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N, 0, -1):
            for j in range(i):
                print("*", end=" ")
            print("")

Solution.printTriangle(None, 5)

'''
Example 1:

Input: 5

Output:
* * * * *
* * * * 
* * * 
* *  
* 
'''

'''
class Solution{
public:
	
	void printTriangle(int n) {
	    // code here
	    for(int i = n; i > 0; i--) {
	        for(int j = 0; j < i; j++) {
	            cout << "* ";
	        }
	        cout << endl;
	    }
	}
};
'''