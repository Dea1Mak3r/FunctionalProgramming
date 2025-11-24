class Solution(object):
    def jump(self, nums):
        n = len(nums)
        
        # Если массив содержит только один элемент, прыжки не нужны
        if n == 1:
            return 0
        
        jumps = 0 
        farthest = 0  # самая дальняя позиция, достижимая с текущим количеством прыжков
        current_end = 0  # конец текущего "уровня" прыжков
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Если уже можем достичь последнего элемента, можем остановиться
                if current_end >= n - 1:
                    break
        
        return jumps

