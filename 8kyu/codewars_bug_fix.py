number = 5

def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i+=1
    return res # Fixed indentation to resolve infinite loop bug


print(create_array(number))
    
