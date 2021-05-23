from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        for i, num in enumerate(nums):
            wanted = target - num
            if wanted in nums_map and nums_map[wanted] != i:
                return i, nums_map[wanted]
            

solution = Solution()
print(solution.twoSum(nums = [2,7,11,15], target = 9))
