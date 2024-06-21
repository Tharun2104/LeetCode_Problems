"""
121. Best Time to Buy and Sell Stock
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""
prices = [7,1,5,3,6,4]
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')
    
        for price in prices:  # TC : O(N)
    
            if price < min_price:  # finding minimum value 
                min_price = price
    
            current_profit = price - min_price  # substracting with other values
            # print(current_profit)
            if current_profit > max_profit:
                max_profit = current_profit
    
        return max_profit
test = Solution()
test.maxProfit(prices)  