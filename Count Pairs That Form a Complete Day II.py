class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        l=len(hours)
        if l<=1:
            return 0
        elif l==2:
            if (hours[0]+hours[1])%24==0:
                return 1
            else:
                return 0
        
        remainder_count={}
        res=0
        for i in hours:
            r=i%24
            c=(24-r)%24
            if c in remainder_count:
                res+=remainder_count[c]
            if r in remainder_count:
                remainder_count[r]+=1
            else:
                remainder_count[r]=1
        return res
        
