def trade_action(current_shares, purchase_price, market_price, available_funds):
    transaction_fee = 10.00
    sufficient_funds = False
    profit_chance = False
    profit = 0
    if available_funds - transaction_fee >= market_price:
        sufficient_funds = True
    if purchase_price > market_price:
        profit_chance = True
    if sufficient_funds == True and profit_chance == True:
        shares_to_buy = int((available_funds - transaction_fee)/ market_price)
        profit = (shares_to_buy * (purchase_price - market_price)) - transaction_fee 
        #print(profit)
        if profit > 0:
            return "Buy " + str(shares_to_buy) + " shares"
        else:
        return "Hold Shares"
    elif purchase_price < market_price:
        if current_shares > 0:
            profit =  current_shares * (market_price - purchase_price) - transaction_fee
            if profit > 0:
                return "Sell " + str(current_shares)+ " shares"
            else:
                return "Hold Shares"
    else:
        return "Hold Shares"
    
print (trade_action(1, 1, 11, 0))