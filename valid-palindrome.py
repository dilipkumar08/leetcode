class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        a=re.sub("[^\W]","",s).lower()
        if a!=a[::-1]:
            return "false"
        else:
            return "true"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for i in s:
            if i.isalnum():
                string+=i
        if string==string[::-1]:
            return "true"
        else:
            return "false"
