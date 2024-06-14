class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=0
        temp=0
        for i in nums:
            temp=i
            print(temp)
            while count[i]>1:

                if temp in count:
                    res+=1
                    temp+=1
                else:
                    count[temp]=1
                    count[i]-=1 
                    break
        return res
        
----------------------------------------------------------------------
#idle

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=0
        temp=0
        for i in range(len(nums)+max(nums)):
            if count[i]>1:
                extra=count[i]-1
                count[i+1]+=extra
                res+=extra
        
        return res
