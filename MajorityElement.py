# 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Follow-up: Could you solve the problem in linear time and in O(1) space?

from typing import List


def majorityElement(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    return nums[n // 2]

# Test Cases

nums = [1, 2, 2, 2, 5, 7, 7]
result = majorityElement(nums)
print(result)