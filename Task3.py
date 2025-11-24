class Solution(object):
    def getRow(self, rowIndex):
        # Если нужна первая строка (rowIndex = 0)
        if rowIndex == 0:
            return [1]
        
        row = [0] * (rowIndex + 1)
        row[0] = 1  # первый элемент всегда 1
        
        # C(n, k) = C(n, k-1) * (n - k + 1) / k
        for i in range(1, rowIndex + 1):
            # Обновляем справа налево, чтобы использовать предыдущие значения
            row[i] = row[i - 1] * (rowIndex - i + 1) // i
            
        return row

