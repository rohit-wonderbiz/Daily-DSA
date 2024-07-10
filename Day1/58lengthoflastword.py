def lengthOfLastWord(s):
    words = s.strip().split() #strip - ermove the spaces, split - converts the string into list of words
    
    if not words:
        return 0
    
    return len(words[-1])

string = "Hello the wod"

output = lengthOfLastWord(string)
print(output)
