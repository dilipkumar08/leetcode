class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li=list(s.split(" "))
        l=len(li)
        p=len(pattern)
        se=set()
        if p<1 and l<1:
            return True
        elif p!=l:
            return False
        elif len(set(li))!=len(set(pattern)):
            return False
        else:
            d={}
            for i in range(l):
                print(i)
                try:
                    d[pattern[i]]+=[li[i]]
                except:
                    d[pattern[i]]=[li[i]]
                print(d[pattern[i]])
                if len(set(d[pattern[i]]))>1:
                    return False
                print(li[i],i,l)
                se.add(li[i])
                print(se)

            if len(se)!=len(d):
                return False
            else:
                return True
            
