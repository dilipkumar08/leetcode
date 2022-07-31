#Make Array Zero by Subtracting Equal Amounts
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)>0 and min(nums)==0:
            nums.remove(0)
        return len(nums)
        
