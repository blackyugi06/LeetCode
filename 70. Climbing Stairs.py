class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        f = [2,3]
        for i in range(3, n):
            f[1], f[0] = f[0] + f[1], f[1]
        return f[1]
        
