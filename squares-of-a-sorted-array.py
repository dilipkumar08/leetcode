class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(x**2 for x in nums))
