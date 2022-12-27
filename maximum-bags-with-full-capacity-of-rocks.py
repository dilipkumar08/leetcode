
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff=[]
        res=0
        for j in range(len(capacity)):
            x=capacity[j]-rocks[j]
            if x==0:
                res+=1
            elif x<=additionalRocks and x!=0:
                diff.append(x)
            
        diff.sort()
        for i in diff:
            if i<=additionalRocks:
                res+=1
                additionalRocks-=i
            else:
                break
        return res
