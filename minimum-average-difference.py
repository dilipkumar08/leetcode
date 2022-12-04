class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l=len(nums)
        if l<2:
            return 0
        else:
            index,value,temp=0,99999,0
            initial=0
            final=sum(nums)
            for i in range(l-1):
                initial+=nums[i]
                final-=nums[i]
                temp=abs((initial//(i+1))-(final//(l-i-1)))
                if temp<value:
                         value=temp
                         index=i
            if sum(nums)//len(nums)<value:
                         index=l-1
            return index
            
