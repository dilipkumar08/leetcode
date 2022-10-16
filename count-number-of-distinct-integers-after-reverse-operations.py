class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        temp=nums.copy()
        r=0
        for i in temp:
            if i%10>=0:
                r=i%10
                i=i//10
                while i>0:
                    r=(r*10)+(i%10)
                    i=i//10
            nums.append(r)
        return len(set(nums))
