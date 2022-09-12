class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l=len(tokens)
        n=0
        i=0
        while True:
            if l==0:
                break
            if l==1 and power<tokens[i]:
                break
            if tokens[i]<=power:
                power=power-tokens[i]
                n+=1
                tokens.pop(i)
                l-=1
            if l<1:
                break
            if n>0 and tokens[i]>power and l>1:
                power+=max(tokens) 
                n-=1
                
        return n
