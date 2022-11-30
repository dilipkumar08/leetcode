#method-1
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lib={}
        for i in arr:
            lib[i]=lib.get(i,0)+1
    
        return len(set(lib.values()))==len(lib)
    
    #method-2
    class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lib={}
        for i in arr:
            lib[i]=lib.get(i,0)+1
        b=list(lib.values())
        for i in b:
            if b.count(i)>1:
                return False
        return True
