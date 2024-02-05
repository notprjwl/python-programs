# Counting the Number of Chocolates.
# Description
# Sanjay loves chocolates. 
# He goes to a shop to buy his favourite chocolate. 
# There he notices there is an offer going on; upon bringing 3 wrappers of the same chocolate, 
# you will get new chocolate for free if Sanjay has m Rupees. 
# How many chocolates will he be able to eat if each chocolate costs c Rupees?

# Sample input:
# 15, 2

# Sample output:
# 10

# Explanation:
# First, he will get 15/2=7 chocolates. 
# He then will return 6 wrappers for 2 chocolates. 
# And lastly, these two wrappers and the one he previously had will get him one more chocolate, making a total of 7+2+1=10 chocolates.

def number_of_chocolates(total_money, cost_of_one):
    if cost_of_one > total_money:
        return "no money"
    else:
        chocolates = total_money // cost_of_one     # total chocolates that he can get
        wrappers = chocolates               # number of wrappers
        while(wrappers // 3 != 0):          # 3 wrappers = 1 chocolate. so wrappers should be >= 3 
            wrappers = wrappers // 3        # number of chocolates we get from wrappers
            chocolates += chocolates % 3 + wrappers    # adding together
    
    return chocolates

print(number_of_chocolates(18, 2)) 
        
            
              