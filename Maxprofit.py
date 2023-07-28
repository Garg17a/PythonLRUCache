def max_profit(prices):
    if not prices or len(prices) == 1:
        return 0
    
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:

        min_price = min(min_price, price)
        # Calculate the profit by selling on the current day
        current_profit = price - min_price
        # Update the maximum profit seen so far
        max_profit = max(max_profit, current_profit)
    
    return max_profit


prices1 = [7, 1, 5, 3, 6, 4]
print(max_profit(prices1))  #output- 5

prices = [7,6,4,3,1]
print(max_profit(prices))  #output - 0
