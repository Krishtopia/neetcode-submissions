class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        max_profit = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right]-prices[left]
                max_profit = max(profit, max_profit)
        
        return max_profit


















        # IT'S PRACTICE TIMEEEE...
        # AND SINCE TOMORROW'S SUNDAY (RN IT IS BUT 1:52 am haha), WE'RE GOING DOUBLE DOWN ON EVERY PROBLEM WE'VE SOLVED SO FAR // TIME TO BUILD THAT MIND MUSCLE //

        # l = 0
        # max_p = 0

        # for r in range(1, len(prices)):
        #     if prices[r] < prices[l]:
        #         l = r
        #     else:
        #         p = prices[r] - prices[l]
        #         max_p = max(max_p, p)
        
        # return max_p
























        # left = 0
        # max_profit = 0

        # for right in range(1, len(prices)):
        #     if prices[right] < prices[left]:
        #         left = right
        #     else:
        #         profit = prices[right] - prices[left]
        #         max_profit = max(max_profit, profit)

        # return max_profit