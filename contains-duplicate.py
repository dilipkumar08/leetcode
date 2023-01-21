ass Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        a=Counter(nums)
        print(a)
        l=len(set(nums))
        s=sum(a.values())
        print(s,l)
        if s>l:
            return True
        else:
            return False            
        
