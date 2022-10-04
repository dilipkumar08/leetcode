class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        n=len(nums1)
        m=n//2
        median=0.0  
        nums1.sort()
        if n%2==0:
            median=(nums1[m]+nums1[m-1])/2
        else:
            median=nums1[m]
        return median
        
        
