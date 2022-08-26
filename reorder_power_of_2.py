class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        i=0
        a=[]
        p=2**i
        while p<=10**9:
            a.append(sorted(str(p)))
            i=i+1
            p=2**i
        return sorted(str(n)) in a
