class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        B=[]
        while True:
            avg=0
            avg=(nums[0]+nums[-1])/2
            B.append(avg)
            nums.pop(0)
            nums.pop(-1)
            if nums==[]:
                break
        return len(set(B))
            
