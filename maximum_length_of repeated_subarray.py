class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        b=[]
        l=len(nums1)
        for i in nums1:
            if i in nums2:
                b.append(i)
                nums2.remove(i)
        lb=len(b)
        if lb==l:
            return lb-1
        else:
            return lb
        
