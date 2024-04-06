class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        score=0
        temp=0
        s=".".join(s)
        li=list(s.split("."))
        for j in range(len(li)):
            if li[j-temp]=='(':
                score+=1
            elif li[j-temp]==')':
                score-=1
            if score==-1:
                li.pop(j-temp)
                score+=1
                temp+=1
        if score!=0:
            l=len(li)-1
        while score!=0:
            if li[l]=="(":
                li.pop(l)
                score-=1
            l-=1
            
        s="".join(li)
        return(s)
        
