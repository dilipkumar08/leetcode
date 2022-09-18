class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        else:
            b=".".join(s)
            b=list(b.split("."))
            l=len(b)
            ae=list(map(ord,b))
            c=[]
            d=1
            i=0
            while True:
                if i+1<l:
                    if ae[i]+1==ae[i+1]:
                        d+=1
                        i+=1
                    else:
                        c.append(d)
                        d=1
                        i+=1
                else:
                    c.append(d)
                    break
            return max(c)
                    
                
                
            
