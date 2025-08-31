prices = [7,6,4,3,1]

def MaxProfit(prices:list[int])-> int:
    # window={'start':0,'end':0}
    # profit=0
    # for i in range(len(prices)):
    #     if prices[window['end']] < prices[i] :
    #         window['end'] = i
    #         profit=max(profit,(prices[window['end']]-prices[window['start']]))
    #     elif prices[window['start']] > prices[i]:
    #         window['end']=window['start'] = i
            
    # return profit

    low,high = prices[0]    
    profit = 0
    for i in prices:
        if i > high:            
            high = i  
        if profit < high-low:
            profit = high-low      
        elif i < low:
            low = i
            high = i       
    return profit
                

print(MaxProfit(prices))
            
        