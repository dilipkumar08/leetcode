class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val=0
        temp=0
        for i in strs:
            try:
                temp=int(i)
            except:
                temp=len(i)
            if temp>max_val:
                max_val=temp
        return max_val
