
# Take input from the user as a string
n = input("Enter the number: ")

# Define the function to check if the number is a Krishnamurthy number
def krishnamurthy(n):
    # Initialize the sum to 0
    sum = 0
    # Iterate over each digit in the input number
    for i in n:
        # Initialize the factorial product to 1
        prod = 1
        # Calculate the factorial of the digit
        for j in range(1, int(i) + 1):
            prod *= j
        # Add the factorial of the digit to the sum
        sum += prod
    # Compare the sum of factorials to the original number
    if sum == int(n):
        print("The number is Krishna Murthy")
    else:
        print("The number is not Krishna Murthy")

# Call the function with the user input
krishnamurthy(n)

