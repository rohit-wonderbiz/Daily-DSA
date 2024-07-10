from collections import defaultdict

# Take input from the user for the first string
s = str(input("Enter String one: "))

# Take input from the user for the second string
t = str(input("Enter String two: "))

# Define the function to check if the two strings are anagrams
def check_anagram(s, t):
    # Initialize a defaultdict to count character occurrences
    count = defaultdict(int)
    
    # Iterate over each character in the first string
    for x in s:
        count[x] += 1
    
    # Iterate over each character in the second string
    for x in t:
        count[x] -= 1
    
    # Check the counts of all characters
    for val in count.values():
        # If any count is not zero, the strings are not anagrams
        if val != 0:
            print("It is not an anagram")
            return False
    
    # If all counts are zero, the strings are anagrams
    print("It is an anagram")
    return True

# Call the function with the user inputs
check_anagram(s, t)
