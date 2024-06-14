class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=0
        temp=0
        for i in count:
            temp=i
            while count[i]>1:
                print(temp,count,res)
                if temp in count:
                    res+=1
                    temp+=1
                else:
                    count[i]-=1 
        
        return res
