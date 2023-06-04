class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        map = {}
        for i in range(N):
            if arr[i] in map:
                map[arr[i]] += 1
            else:
                map[arr[i]] = 1
          
        for i in range(1, N + 1):
            if i in map:
                arr[i - 1] = map[i]
            else: arr[i - 1] = 0

        return arr
        
    
print(Solution.frequencyCount(None, [2, 3, 2, 3, 5], 5, 5))