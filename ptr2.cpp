class Solution
{
public:
    void printTriangle(int n)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                cout << "* ";
            }
            cout << endl;
        }
    }
};

/*
Example 1:

Input: 5

Output:
* 
* * 
* * * 
* * * * 
* * * * *
*/

// #User function Template for python3

// class Solution:
//     def printTriangle(self, N):
//         # Code here
//         for i in range(1, N + 1):
//             for j in range(i):
//                 print("* ", end="")
//             print("")