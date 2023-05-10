class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(1, 2 * N):
            for j in range(1, 2 * N):
                min_dist = min(i - 1, j - 1, 2 * N - i - 1, 2 * N -j - 1)
                num = N - min_dist
                print(num, end=' ')
            print()


Solution.printTriangle(None, 4)

'''
Input: 4

Output:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''
