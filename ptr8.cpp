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
			for (int i = n; i > 0; i--)
			{
				for (int j = 0; j < n - i; j++)
				{
					cout << " ";
				}
				for (int k = 2 * i - 1; k > 0; k--)
				{
					cout << "*";
				}
				cout << endl;
			}
		}
	};

	Solution obj;
	obj.printTriangle(5);
	// system("pause");
	return 0;
}

/*
Input: 5

Output:

*********
 *******
  *****
   ***
	*
*/

/*
class Solution:
	def printTriangle(self, N):
		# Code here
		for i in range(N, 0, -1):
			for j in range(N - i):
				print("", end=" ")
			for k in range(2 * i - 1, 0, -1):
				print("*", end="")
			print("")
*/