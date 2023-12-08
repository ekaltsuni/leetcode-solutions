# 125 Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
import re


def isPalindrome(s: str) -> bool:
    string = s.lower()
    string = re.sub('[^A-Za-z0-9]+', '', string)
    i = 1
    for i in range(len(string)):
        if string[0] == string[-1] and string[i] == string[-i-1]:
            i += 1
            return True
        else:
            return False

# Test Cases

s = "race a car"

#s = "A man, a plan, a canal: Panama"
result = (isPalindrome(s))
print(result)