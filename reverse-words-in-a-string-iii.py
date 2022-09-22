class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s.split(" "))
        l=len(s)
        for i in range(l):
            s[i]=s[i][::-1]
        return " ".join(s)
        
