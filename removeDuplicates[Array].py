# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements
# in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    j = i + 1
    k = len(nums)
    nums.sort()

    while i < len(nums)-1:
        if nums[i] == nums[j]:
            nums.remove(nums[j])
            j = i + 1
        else:
            i += 1
            j = i + 1
    k = len(nums)
    return k

# Test Cases

nums = [1, 1, 2, 3, 5, 5, 7, 8, 8]
result = removeDuplicates(nums)
print(result)
