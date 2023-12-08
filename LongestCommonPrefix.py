# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    answer = ""
    strs = sorted(strs)
    print(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return answer
        answer += first[i]
    return answer

# Test Cases

strs = ["flower", "flow", "flight", "fling"]
result = longestCommonPrefix(strs)
print(result)