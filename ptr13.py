class Solution:
    def printTriangle(self, N):
        # Code here
        x = 1
        for row in range(1, N + 1):
            for line in range(1, row + 1):
                print(x, end=" ")
                x += 1
            print("")

ptr13 = Solution
ptr13.printTriangle(None, 5)

'''
Input: 5

Output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''

'''
x = 1;
for (int i = 1; i <= n; i++)
{
    for (int j = 1; j <= i; j++)
    {
        cout << x << " ";
        x++;
    }
    cout << endl;
}
'''