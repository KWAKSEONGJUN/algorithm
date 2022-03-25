from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            left, right, product = 0, len(nums)-1, 1
            
            while left < right:
                if left == i:
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue
                else:
                    product *= nums[left] * nums[right]
                    left += 1
                    right -= 1
                
            if left == right and left != i:
                product *= nums[left]
                
            res.append(product)
            
        return res
        
        
        
solution = Solution()
solution.productExceptSelf([-1,1,0,-3,3])