from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
        
solution = Solution()
solution.arrayPairSum([6,2,6,5,1,2])