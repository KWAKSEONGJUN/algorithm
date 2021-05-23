import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = re.sub(r'[^a-zA-Z0-9]', '', s)
        str = ''.join(str).lower()
        print(str)
        if str == str[::-1]:
            return True

        return False


solution = Solution()
print(solution.isPalindrome("ab_a"))
