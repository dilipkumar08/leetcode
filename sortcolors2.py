
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        temp=[0,0,0]
        for i in nums:
            temp[i]+=1
        for j in range(3):
            for k in range(temp[j]):
                nums.pop(0)
                nums.append(j)
