Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set()

        for num in nums:
            if num in unique_elements:
                return True
            unique_elements.add(num)
        return False
solution = Solution()
result = solution.containsDuplicate([1,2,3,1])
print(result)  

"logic 2:"

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):e is foun
            if nums[i] == nums[i - 1]:
                return True
        return False
