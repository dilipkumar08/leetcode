class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m=s.count("0")
        res=m
        if m==0:
            return 0
        else:
            for i in s:
                if i=="0":
                    m-=1
                    res=min(m,res)
                else:
                    m+=1
            return res
