class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=nums
        for i in temp:
            d=target-i
            n=0
            ind=temp.index(i)
            temp[temp.index(i)]=None
            if d in nums[n+1:]:
                o=list([ind,temp.index(d)])
                return o
            n+=1
