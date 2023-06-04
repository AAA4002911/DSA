class Solution:
    def armstrongNumber (ob, n):
        # code here
        n_cpy = n
        neg_flag = 1
        if n_cpy < 0:
            neg_flag = -1
            n_cpy = -1 * n_cpy
        arm_strong = 0
        while n_cpy != 0:
            rem = n_cpy % 10
            arm_strong += rem ** 3
            n_cpy = n_cpy // 10
        return 'Yes' if arm_strong * neg_flag == n else 'No'

print(Solution.armstrongNumber(None, 153))