class Solution:
    def maxDepth(self, s: str) -> int:
        max=0
        temp=0
        for i in s:
            if i=="(":
                temp+=1
            elif temp!=0 and i==")":
                temp-=1
            if max<temp:
                max=temp
        return max

