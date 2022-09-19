class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c=len(changed)
        a=int(c/2)
        if c%2==0:
            return changed[0:a]
        else:
            return []
       
