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
class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            for j in range(N - i):
                print(" ", end="")
            for k in range(2 * i + 1):
                print("*", end="")
            print("")
'''