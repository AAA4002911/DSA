class Solution:
    def lcmAndGcdItr(self, A , B):
        # BruteForce Approach
        n = min(A, B)
        gcd = 1
        for i in range(1, n + 1):
            if A % i == 0 and B % i == 0:
                gcd = i
        
        lcm = int((A * B) / gcd)
                
        return '{} {}'.format(lcm, gcd)
    
    def lcmAndGcd(self, A, B):
        gcd = self.gcd(A, B)
        lcm = int((A * B) / gcd)
        return '{} {}'.format(lcm, gcd)

    def gcd(self, A, B):
        if B == 0: return A
        return self.gcd(B, A % B)
# print(Solution.lcmAndGcdItr(None, 5, 10))

obj = Solution()
result = obj.lcmAndGcd(5, 10)
print(result)

