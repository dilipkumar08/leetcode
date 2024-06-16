class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        upto=0
        i=0
        res=0

        N=len(nums)
        while upto<n:
            if i<N and nums[i]<=upto+1:
                upto+=nums[i]
                i+=1
            else:
                upto+=(upto+1)
                res+=1
        return res
