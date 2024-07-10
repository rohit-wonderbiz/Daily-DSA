# Anagram Checker

This Python script checks whether two given strings are anagrams. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## How It Works

1. The script prompts the user to enter two strings.
2. It defines a function `check_anagram` to determine if the two strings are anagrams.
3. Inside the function:
   - It initializes a `defaultdict` to count the occurrences of each character in both strings.
   - It iterates over each character in the first string, incrementing the count for each character.
   - It iterates over each character in the second string, decrementing the count for each character.
   - It checks the counts of all characters. If any count is not zero, the strings are not anagrams.
4. Based on the character counts, it prints whether the strings are anagrams or not.
