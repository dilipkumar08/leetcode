#my solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        for i in range(len(nums)):
            if j<len(nums):
                if nums.count(nums[j])>1:
                    nums.remove(nums[j])
                else:
                    j+=1
            else:
                break
        return len(nums)
      
      
      
 #idle solution
nums=[1,1,1,4,2,1]
l=1
for r in range(1, len(nums)):
    if nums[r] != nums[r-1]:
        nums[l] = nums[r]
        l += 1
return l
