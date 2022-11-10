class Solution:
    def removeDuplicates(self, s: str) -> str:
        i=0
        s=list(x for x in s)
        l=len(s)
        while i<l:
            try:
                if s[i]==s[i+1]:
                    s.pop(i+1)
                    s.pop(i)
                    if i>1:
                        i-=2
                    elif i==1:
                        i-=1    
                else:
                    i+=1
            except:
                break
        return "".join(s)
