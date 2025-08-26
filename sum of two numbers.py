from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i

nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, target)) 


# Key points:
# 1. Brute Force:
#    - Nested loops; inner loop starts from i+1
#    - Avoids using the same element twice (i != j)
#    - Avoids duplicate pairs ((i, j) and (j, i))
#    - Reduces number of iterations
#    - Time complexity: O(n²), Space complexity: O(1)
#
# 2. enumerate usage:
#    - for i, num in enumerate(nums):
#        i   → index
#        num → value
#    - Retrieves index and value simultaneously, cleaner code
#
# 3. Python variable definition mechanism:
#    - Python is dynamically typed; variables are created on first assignment
#    - In for loops, i and num are auto-assigned per iteration
#
# 4. Hashmap (dictionary):
#    - hashmap = {} creates an empty dictionary
#    - Store: key = number, value = index
#    - For each num:
#        complement = target - num
#        If complement in hashmap → return [hashmap[complement], i]
#        Else store num with its index
#    - Time complexity: O(n), Space complexity: O(n)