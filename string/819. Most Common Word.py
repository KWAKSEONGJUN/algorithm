import re
import collections

class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() \
            if word not in banned]
        
        counts = collections.Counter(words) 
        return counts.most_common(1)[0][0]
       
                
solution = Solution()
p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]
solution.mostCommonWord(p, b)
        