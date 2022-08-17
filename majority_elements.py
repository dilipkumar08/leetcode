class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        nums=Counter(nums)
        a=list(nums.keys())
        b=list(nums.values())
        i=b.index(max(b))
        return a[i]
        
