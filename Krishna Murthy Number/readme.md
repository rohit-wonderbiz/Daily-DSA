# Krishnamurthy Number Checker

This Python script checks whether a given number is a Krishnamurthy number. A Krishnamurthy number (or a strong number) is a number for which the sum of the factorials of its digits is equal to the number itself.

## How It Works

1. The script prompts the user to enter a number.
2. It defines a function `krishnamurthy` to determine if the entered number is a Krishnamurthy number.
3. Inside the function:
   - It initializes a variable `sum` to 0.
   - It iterates over each digit of the input number.
   - For each digit, it calculates its factorial.
   - It adds the factorial of each digit to the `sum`.
4. After calculating the sum of the factorials of the digits, it compares this sum to the original number.
5. The script prints whether the number is a Krishnamurthy number or not.

<!-- ## Code

```python
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
krishnamurthy(n) -->
