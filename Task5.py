class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        
        # Если массив пустой или содержит один элемент, прибыли быть не может
        if n < 2:
            return 0
            
        # Если цена растет от дня i к дню i+1, покупаем в день i и продаем в день i+1
        max_profit = 0
        
        for i in range(n - 1):
            if prices[i + 1] > prices[i]:
                max_profit += prices[i + 1] - prices[i]
        
        return max_profit

