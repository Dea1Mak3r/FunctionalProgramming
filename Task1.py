class Solution(object):
    def climbStairs(self, n):

        # Базовые случаи
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev = 1  # количество способов для ступеньки 1
        curr = 2  # количество способов для ступеньки 2
        
        for i in range(3, n + 1):
            next_val = prev + curr
            prev = curr
            curr = next_val
        
        return curr

