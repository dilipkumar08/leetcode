#Mryhod-1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap={}
        
        for i,n in enumerate(nums):
            diff=target-n
            if diff in Hmap:
                return [Hmap[diff],i]
            else:
                Hmap[n]=i
        return 
 
#Method-2
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
