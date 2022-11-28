from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matches=list(zip(*matches))
        winners=set(matches[0])
        lossers=Counter(matches[1])
        ans_0,ans_1=[],[]
        for i in winners:
            if i not in lossers:
                ans_0.append(i)
        for j in lossers:
            if lossers[j]==1:
                ans_1.append(j)
        
        return [sorted(ans_0),sorted(ans_1)]
        
            
