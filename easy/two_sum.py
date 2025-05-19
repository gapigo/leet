# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        assert len(nums) >= 2 and len(nums) <= 1e4, 'List size needs to be larger or equal as two and smaller or equal as 10.000'
        assert not any([x for x in nums if abs(x) >= 1e9]) and abs(target) <= 1e9, 'Neither target nor elements of the list can be larger than 1 billion (10^e9)'
        indexes = []
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i != j:
                    if x + y == target:
                        indexes = [i, j]
                        break
            if len(indexes): break
        return indexes

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([3,2,4], 6))
    print(s.twoSum([3,3], 6))