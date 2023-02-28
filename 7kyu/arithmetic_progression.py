#In your class, you have started lessons about arithmetic progression. Since you are also a programmer, you have decided to write a function that will return the first n elements of the sequence with the given common difference d and first element a. Note that the difference may be zero!

#The result should be a string of numbers, separated by comma and space.


#my solution

def arithmetic_sequence_elements(a, d, n):
    
    # Create an empty list to store the progression
    progression = []
    
    # Add the first term to the list
    progression.append(a)
    
    # Loop n-1 times to add the remaining terms to the list
    for i in range(1, n):
        
        # Calculate the next term and add it to the list
        progression.append(a + i*d)
        
    # Convert the list to a string, separated by comma and space
    return ', '.join(str(term) for term in progression)