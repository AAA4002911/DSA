class Solution:
    def printTriangle(self, N):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(1, N + 1):
            for j in range(1, i + 1):
                print(letters[N - j], end=" ")
            print("")

Solution.printTriangle(None, 5)
        

'''
Input: 5

Output:
E
E D
E D C
E D C B
E D C B A
'''

'''
for(int i = 1; i <= n; i++)
{
    for(char j= 'A' + n - 1; j >= 'A' + n - i; j--)
    {
        cout << j << " ";
    }
cout << endl;
}
'''