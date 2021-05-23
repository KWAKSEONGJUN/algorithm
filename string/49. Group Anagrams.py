from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        
        for str in strs:
            group[''.join(sorted(str))].append(str)
        
        return group.values()
        
        
    
    
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))