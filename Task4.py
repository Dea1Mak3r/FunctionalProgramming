class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        # Если массив пустой или содержит один элемент, прибыли быть не может
        if n < 2:
            return 0
        
        # Используем жадный алгоритм
        # Отслеживаем минимальную цену покупки и максимальную прибыль
        min_price = prices[0]  # минимальная цена для покупки
        max_profit = 0  # максимальная прибыль
        
        # Проходим по всем ценам начиная со второго дня
        for i in range(1, n):
            # Обновляем минимальную цену покупки
            min_price = min(min_price, prices[i])
            
            # Вычисляем потенциальную прибыль от продажи в текущий день
            current_profit = prices[i] - min_price
            
            # Обновляем максимальную прибыль
            max_profit = max(max_profit, current_profit)
        
        return max_profit

