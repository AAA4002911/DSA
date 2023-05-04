class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N, 0, -1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print("")


'''
Example 1:

Input: 5

Output:
1 2 3 4 5
1 2 3 4
1 2 3 
1 2  
1 
'''


'''
class Solution{
public:
	
	void printTriangle(int n) {
	    // code here
	    for(int i = n; i > 0; i--) {
	        for(int j = 1; j <= i; j++) {
	            cout << j << " ";
	        }
	        cout << endl;
	    }
	}
};
'''