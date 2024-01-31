Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1

"logic 2:"

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target
                    return [i, j]
        return []
