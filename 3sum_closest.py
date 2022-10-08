class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=len(nums)
        three_sums=[]
        d=dict()
        c=0
        for i in range(l):
            s=0
            if i+3<l:
                s=sum(nums[i:i+3])
                three_sums.append(s)
                c+=1
            else:
                break
        for j in range(c):
            d[three_sums[j]]=abs(target-three_sums[j])
        for key,values in d.items():
            return (key)
            break
                
                
                 
            
