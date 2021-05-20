import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = re.findall(r'[A-z]', s)
        str = ''.join(str)
        
        if s == str[::-1]:
            return True

        return False


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
