class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ans = speedSum = 0
        heap = []
        
		# sort engineers by decreasing efficiency
		# Eg.: speed: [2, 10, 3, 1 ,5, 8] and efficiency: [5, 4, 3, 9, 7, 2]
        # after sort, it becomes
        # candidates: [(9, 1), (7 ,5), (5, 2), (4, 10), (3, 3), (2, 8)]

        for engineer in sorted(zip(efficiency, speed), reverse = True):                
            eff, spd = engineer
			
			# accumulate speed of selected engineer and add engg. into the pool
            speedSum += spd
            ans = max(ans, speedSum  * eff)
            heappush(heap, spd)
            
			# Size of heap cant become more than k - 1, since we add 1 engineer in the next iteration
			# eliminate the engineers with minimum speed
            while len(heap) > k - 1:
				# decrease the accumulated speedSum
                speedSum -= heappop(heap)
            
        
        return ans % (10**9+7)
