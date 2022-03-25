from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        stack = []
        for i, h in enumerate(height):
            if not stack:
                stack.append(i)
                continue

            if height[stack[-1]] >= h:
                stack.append(i)
            else:
                while stack and height[stack[-1]] <= h:
                    pi = stack.pop()
               
                stack.append(i)
                mx = max(height[pi], height[i])
                for j in range(pi, i):
                    sum += mx - height[j]
                    height[j] += mx - height[j]
                    
        return sum
                    
                
    
solution = Solution()
print(solution.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])) 