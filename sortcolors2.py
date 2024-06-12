
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        temp=[0,0,0]
        for i in nums:
            temp[i]+=1
        for j in range(3):
            for k in range(temp[j]):
                nums.pop(0)
                nums.append(j)

---------------------------------------------------------------------
#idle solution 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,r=0,len(nums)-1
        i=0

        while i<=r:
            if nums[i]==0:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
            elif nums[i]==2:
                nums[r],nums[i]=nums[i],nums[r]
                r-=1
                i-=1

            i+=1
