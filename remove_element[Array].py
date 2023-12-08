# 27. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted,
# you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
from typing import List


def removeElement(nums:List[int], val:int) -> int:
    i = 0
    k = len(nums)
    while i < k:
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    k = len(nums)
    return k


# Test Cases

nums = [1, 2, 3, 4, 5, 3]
val = 3
result = removeElement(nums, val)
print(result)