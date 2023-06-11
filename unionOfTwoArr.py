'''
Union of two arrays can be defined as the common and distinct elements in the two arrays.
Given two sorted arrays of size n and m respectively, find their union.


Example 1:

Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 3, arr2 [] = {1, 2, 3}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.

 

Example 2:

Input: 
n = 5, arr1[] = {2, 2, 3, 4, 5}  
m = 5, arr2[] = {1, 1, 2, 3, 4}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.

 

Example 3:

Input:
n = 5, arr1[] = {1, 1, 1, 1, 1}
m = 5, arr2[] = {2, 2, 2, 2, 2}
Output: 1 2
Explanation: Distinct elements including 
both the arrays are: 1 2.


Your Task: 
You do not need to read input or print anything. Complete the function findUnion() that takes two arrays arr1[], arr2[], and their size n and m as input parameters and returns a list containing the union of the two arrays. 
 

Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(n+m).
 

Constraints:
1 <= n, m <= 105
1 <= arr[i], brr[i] <= 106

'''


class Solution:

    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b, n, m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here
        result = []
        i = j = 0

        while i < n and j < m:
            if a[i] < b[j]:
                if not result or a[i] != result[-1]:
                    result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if not result or b[j] != result[-1]:
                    result.append(b[j])
                j += 1
            else:
                if not result or a[i] != result[-1]:
                    result.append(a[i])
                i += 1
                j += 1

        while i < n:
            if not result or a[i] != result[-1]:
                result.append(a[i])
            i += 1

        while j < m:
            if not result or b[j] != result[-1]:
                result.append(b[j])
            j += 1

        return result


obj = Solution()
res = obj.findUnion([1, 2, 3, 4, 5], [1, 2, 3], 5, 3)
print("Union Array:", res)
