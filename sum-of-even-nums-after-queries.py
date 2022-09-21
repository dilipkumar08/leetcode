class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=0
        for i in nums:
            if i%2==0:
                s+=i
        res=[]
        for val,ind in queries:
            if nums[ind]%2==0:
                s-=nums[ind]
            nums[ind]+=val
            if nums[ind]%2==0:
                s+=class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        l=len(nums)
        res=[]
        for i in range(l):
            sum=0
            nums[queries[i][1]]=nums[queries[i][1]]+queries[i][0]
            for j in range(l):
                if nums[j]%2==0:
                    sum+=nums[j]
            res.append(sum)
                    
            
        return resnums[ind]
            res.append(s)
                    
            
        return res
      
      
