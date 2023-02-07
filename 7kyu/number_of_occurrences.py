#Write a function that returns the number of occurrences of an element in an array.

# mySolution

def number_of_occurrences(element, sample): #this is a function number_of_occurrences that take two arguments
   
    count = 0    #we then made variable count which we initialized to 0.We will later on use variable count to keep track of the number of occurrences of element in sample.
    
    for i in sample: # for loop that will iterate through each element i in the list sample.
       
        if element == i: #if element is equal to the current iteration variable i. If this condition is True, then the code inside the if block will be executed.
          
            count += 1 #if the if condition is True, this line will increase the value of count by 1.
   
    return count
        
