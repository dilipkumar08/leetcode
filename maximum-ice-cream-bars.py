class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res=0
        costs.sort()
        for i in costs:
            if i<=coins:
                coins-=i
                res+=1
            else:
                break
        return res
