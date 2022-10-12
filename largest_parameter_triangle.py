class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        l=len(nums)
        m=l
        while l> 2 and nums[0] >= nums[1] + nums[2]:
            nums.pop(0)
            l-=1
            
        return 0 if l < 3 else sum(nums[:3])
