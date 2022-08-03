class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False
-------------------------------------------------------------------------------
class Solution:
    def isPalindrome(self, x: int) -> bool:
    return str(x)==str(x)[::-1]
