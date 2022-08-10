class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=list(map(str,s.strip().split()))
        return len(a[len(a)-1])
