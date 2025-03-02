class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
        # maxProfit = 0
        # for i in range(0,len(prices)):
        #     for j in range(i,len(prices)):
        #         maxProfit = max(maxProfit,prices[j]-prices[i])
        # return maxProfit

        #O(n) time complexity
        #maintain 3 vars for buying, selling the stock
        #and keeping track of profit to gain maxProfit
        buy = prices[0]
        sell = 0
        maxProfit = 0
        for i in range(1,len(prices)):
            #update the buy var if any lower var encounters in the process
            if prices[i] < buy:
                buy = prices[i]
            #if there is any prices[i] that is greater than or equal to 
            #prices calculate the maxProfit
            else:
                sell = prices[i]
                maxProfit = max(maxProfit,sell-buy)
        return maxProfit

                
        