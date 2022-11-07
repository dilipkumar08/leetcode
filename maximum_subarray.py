#Method-1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        cu=0
        for i in nums:
            if cu<0:
                cu=0
            cu+=i
            res=max(res,cu)
        return res
      
  #Method-2
  class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c=0
        m=float("-inf")
        for i in nums:
            c=max(c+i,i)
            m=max(c,m)
        return m
