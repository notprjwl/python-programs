# def maxProfit(prices):
#     minNum = prices[0]
#     maxNum, profit = 0, 0
    
#     for i in range(len(prices)):
#         if prices[i] < minNum:
#             minNum = prices[i]
#             # print(prices[i])
#     # print(minNum)

        
#     maxNumIdx = prices.index(minNum) + 1
#     for i in range(maxNumIdx, len(prices)):
#         if prices[i] > maxNum:
#             maxNum = prices[i]
#     # print(maxNum)
            
#     if not maxNum: 
#         return 0
    
#     profit = maxNum - minNum      
#     return profit

# print(maxProfit([4,1,5,2,7]))


# PASSED SOLUTION
def maxProfit(prices):
    left = prices[0]
    maxProfit = 0
    currProfit = 0
    for i in range(1, len(prices)):
        right = prices[i]
        if right < left: 
            left = right
        else:
            currProfit = right- left
            maxProfit = max(maxProfit, currProfit)
    
    return maxProfit
            
print(maxProfit([7,1,5,3,6,4]))
