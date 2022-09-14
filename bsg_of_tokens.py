class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l=len(tokens)
        n=0
        i=0
        if l==0:
            n=0
        elif min(tokens)>power:
            n=0
        else:
            while True:
                if tokens[i]<=power:
                    power=power-tokens[i]
                    n+=1
                    tokens.pop(i)
                    l-=1
                    if l==1 and tokens[i]>power:
                        break
                    if l==0:
                        break
                if n>0 and tokens[i]>power and l>1:
                    power+=tokens[l-1]
                    tokens.remove(tokens[l-1])
                    l-=1
                    n-=1
                
                
        return n
