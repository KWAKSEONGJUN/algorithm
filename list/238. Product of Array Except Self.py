from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            print(i)
            left, right, product = 0, len(nums)-1, 1
            
            while left < right:
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue
                
                product *= nums[left] * nums[right]
                
            if left == right:
                product *= nums[left]
                
            res.append(product)
            
        return res
        
        
        
solution = Solution()
solution.productExceptSelf([1, 2, 3, 4])