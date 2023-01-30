# There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a given quantity and price (per mango), calculate the total cost of the mangoes.

# Examples
# mango(2, 3) ==> 6    # 2 mangoes for $3 per unit = $6; no mango for free
# mango(3, 3) ==> 6    # 2 mangoes for $3 per unit = $6; +1 mango for free
# mango(5, 3) ==> 12   # 4 mangoes for $3 per unit = $12; +1 mango for free
# mango(9, 5) ==> 30   # 6 mangoes for $5 per unit = $30; +3 mangoes for free

# my solution


# we have a function called mango which has two parameters, quantity and price.
def mango(quantity, price): 
    # 3 for 2 offer which means ther is one mango for free
    # we then need to return the price of the mangoes
    
    quantity = quantity - (quantity // 3)  
    # then the (quantity // 3) is actually the remainder which is the mango/es we are given for free after buying
    # thus if we buy 12 mangoes it means we actually have 3 more mangoes for free
    
    return quantity * price
    # then we now multiply our quantity by the price as it will be the total cost of the mangoes !!
    
