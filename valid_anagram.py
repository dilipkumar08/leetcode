#Method-1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
      
#Method-2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)

#Method-3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=len(s)
        T=len(t)
        if l!=T:
            return False
        else:
            counts,countt={},{}
            for i in range(l):
                counts[s[i]]=1+counts.get(s[i],0)
                countt[t[i]]=1+countt.get(t[i],0)
            for c in counts:
                if counts[c]!=countt.get(c,0):
                    return False
        return True
