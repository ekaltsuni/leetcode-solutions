# 28. Find the Index of the First Occurrence in a String

# Given two strings "needle" and "haystack", return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

def strStr(haystack: str, needle: str) -> int:
    i = 0
    for i in range(len(haystack)):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
    i += 1

# Test Cases

haystack = "hello"
needle = "ll"
result = strStr(haystack, needle)
print(result)