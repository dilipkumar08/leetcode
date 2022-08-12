class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        a=re.sub("[^\W]","",s).lower()
        if a!=a[::-1]:
            return "false"
        else:
            return "true"
