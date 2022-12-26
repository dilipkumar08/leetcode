class Solution:
    def canJump(self, nums: List[int]) -> bool:
        counter = len(nums)-1
        for i in range(counter, -1, -1):
            if counter-i <= nums[i]: counter = i
        return counter == 0
