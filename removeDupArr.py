class Solution:
    def remove_duplicate(self, A, N):
        i = 0
        for j in range(1, len(A)):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
        return i + 1


print(Solution.remove_duplicate(None, [2, 2, 2, 2, 2], 5))
