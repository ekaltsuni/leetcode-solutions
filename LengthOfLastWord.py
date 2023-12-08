# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s: str) -> int:

    arrayText = s.split(" ")
    print(arrayText)
    i = 0
    newArrayText = []
    while i < len(arrayText):
        if arrayText[i] != "":
            newArrayText.append(arrayText[i])
        i += 1
    print(newArrayText)
    return len(newArrayText[-1])

# Test Cases

s = "   fly me   to   the moon  "
result = lengthOfLastWord(s)
print(result)

