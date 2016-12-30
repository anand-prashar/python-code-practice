
'''
Created on Dec 28, 2016

@author: anand
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        gap = 0
        low = prices[0]
        for i in range(1, len(prices)):
            if low > prices[i]: low = prices[i]
            if gap < (prices[i]-low):
                gap = (prices[i]-low)

        return gap

obj = Solution()
obj.maxProfit([7, 1, 5, 3, 6, 4])        