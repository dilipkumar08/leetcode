class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        a=Counter(nums)
        if 2 in a.values():
            return 'true'
        else:
            return 'false'
            
        
