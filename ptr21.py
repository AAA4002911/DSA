class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            if i == 0 or i == N - 1:
                for j in range(N):
                    print("*", end="")
            else:
                for j in range(N):
                    if j == 0 or j == N - 1:
                        print("*", end="")
                    else:
                        print(" ", end="")
            print("")

Solution.printTriangle(None, 5)
                 


'''
Input: 4

Output:
****
*  *
*  *
****
'''