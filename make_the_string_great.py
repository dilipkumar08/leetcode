class Solution:
    def makeGood(self, s: str) -> str:
        li=list(x for x in s)
        l=len(li)
        i=0
        if l==2:
            if li[i]==li[i+1].upper() or li[i].upper==li[i+1] :
                return ""
            else:
                return s
        
        while i+1<l:
            if li[i+1]==li[i].upper() :
                li.pop(i+1)
                li.pop(i)
                l-=2
                i-=2
            elif l==2 and li[i]==li[i-1].upper():
                li.pop(i-1)
                li.pop(i)
                l-=2
                i-=1
            if l==0:
                break
            i+=1
        return str("".join(li))
