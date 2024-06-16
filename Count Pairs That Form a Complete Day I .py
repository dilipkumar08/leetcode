class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        res=0
        l=len(hours)
        if l<=1:
            return 0
        elif l==2:
            if (hours[0]+hours[1])%24==0:
                return 1
            else:
                return 0
        
        for i in range(l):
            for j in range(i+1,l):
                if (hours[i]+hours[j])%24==0:
                    res+=1
        return res
