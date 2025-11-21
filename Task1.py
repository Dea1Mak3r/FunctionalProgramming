class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Базовые случаи
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Используем динамическое программирование
        # Количество способов достичь ступеньки i равно сумме способов
        # достичь ступенек (i-1) и (i-2)
        # Оптимизировано по памяти: O(1) вместо O(n)
        prev = 1  # количество способов для ступеньки 1
        curr = 2  # количество способов для ступеньки 2
        
        for i in range(3, n + 1):
            next_val = prev + curr
            prev = curr
            curr = next_val
        
        return curr

