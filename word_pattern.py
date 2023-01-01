class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li=list(s.split(" "))
        l=len(li)
        p=len(pattern)
        if p<1 and l<1:
            return True
        elif p!=l:
            return False
        else:
            d={}
            for i in range(len(li)):
                try:
                    d[pattern[i]]+=[li[i]]
                except:
                    d[pattern[i]]=[li[i]]
                if len(set(d[pattern[i]]))>1:
                    return False
            if len(set(d.values()))!=len(d):
                return False
            else:
                return True
            
