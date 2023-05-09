class Solution:
    def printTriangle(self, N):
        for row in range(1, N + 1):
            start = 1
            for digit in range(1 , row + 1):
                print(start, end=" ")
                start += 1
            for empty in range(1, 2 * N - 2 * row + 1):
                print(" ", end=" ")
            for digit in range(1 , row + 1):
                start -= 1
                print(start, end=" ")
            print("")


ptr12 = Solution
ptr12.printTriangle(None, 5)


'''
Input: 5

Output:
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1
'''

'''
for(int i = 1 ; i <= n ; i++)
{
    for(int j = 1 ; j <= i ; j++)
    {
        cout<<j<<" ";
    }
    for(int k = n ; k >= 1 ; k--)
    {
        if( k <= i ) { cout << k << " "; }
        else { cout << "    "; }
    }
    cout<<endl;
}
'''