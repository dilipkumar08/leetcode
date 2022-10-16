class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg=[]
        pos=[]
        res=0
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        neg=list(sorted(set(neg)))
        pos=list(set(pos))
        for j in neg:
            a=abs(j)
            if a in pos:
                res=a
                break
        if res!=0:
            return res        
        else:
            return -1
