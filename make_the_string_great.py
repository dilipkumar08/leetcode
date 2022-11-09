class Solution:
    def makeGood(self, s: str) -> str:
        li=list(x for x in s)
        l=len(li)
        i=0
        while i<l:
            try:
                if li[i]!=li[i+1]:
                    if li[i+1]==li[i].upper() or li[i+1].upper() == li[i]:
                        li.pop(i+1)
                        li.pop(i)
                        i=0
                        l-=2
                    else:
                        i+=1
                else:
                    i+=1
            except:
                break
            
        return str("".join(li))
