class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxprofit=[]
        mincap=[(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(mincap)
        for i in range(k):
            while mincap and mincap[0][0]<=w:
                c,p=heapq.heappop(mincap)
                heapq.heappush(maxprofit,-1*p)
            if not maxprofit:
                break
            w+=-1*heapq.heappop(maxprofit)
        return w  
