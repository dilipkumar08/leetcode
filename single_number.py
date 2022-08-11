class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)==1:
                break
        return i
            
                
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1:
            return nums[0]
        else:
            nums.sort()
            for i in range(l):
                if i==0:
                    if nums[i]!=nums[i+1]:
                        break
                elif i==l-1:
                    if nums[l-2]!=nums[l-1]:
                        break
                elif 0<i<l-1:
                    if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
                        break
        return nums[i]
                    
            
                
