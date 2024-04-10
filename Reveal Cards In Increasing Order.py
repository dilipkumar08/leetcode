class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        l=len(deck)
        result=[1]*l
        sample=[j for j in range(l)]
        a=0
        for i in deck:
            a=sample.pop(0)
            result[a]=i
            if sample:
                sample.append(sample.pop(0))
        return result
