class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        a=""
        a=re.findall("[A-Za-z0-9]",s)
        a="".join(a).lower()
        return a==a[::-1]
            
