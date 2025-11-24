class Solution(object):
    def maxProfit(self, prices):
        
        n = len(prices)
        
        # Если массив пустой или содержит один элемент, прибыли быть не может
        if n < 2:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            current_profit = prices[i] - min_price            
            max_profit = max(max_profit, current_profit)
        
        return max_profit

