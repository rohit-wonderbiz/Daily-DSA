# Take input from the user for the number of bottles
nb = input("Enter the number of bottles: ")

# Take input from the user for the number of bottles needed for an exchange
ne = input("Enter the number of bottles exchanges: ")

# Define the function to calculate the total number of bottles that can be consumed
def water(nb, ne):
    # Initialize the result to 0 to keep track of the total bottles consumed
    result = 0
    
    # Initialize full to the number of initial bottles
    full = int(nb)
    
    # Initialize empty to 0 to keep track of empty bottles
    empty = 0
    
    # While there are full bottles
    while full:
        # Add the number of full bottles to the result
        result += full
        
        # Add the number of full bottles to empty
        empty += full
        
        # Calculate the number of new full bottles from exchanging empty bottles
        exchange = empty // int(ne)
        
        # Update full to the number of new full bottles
        full = exchange
        
        # If the exchange rate results in full bottles being the same as exchange, reset empty bottles
        if exchange == full:
            empty = 0
        else:
            # Reduce the empty bottles by the number of bottles used in the exchange
            empty -= (int(ne) * full)
    
    # Return the total number of bottles consumed
    return result

# Call the function with the user inputs and store the output
output = water(nb, ne)

# Print the output
print(output)
