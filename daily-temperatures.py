#efficient method which actually works monotonics stack 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for  i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackInd =stack.pop()
                res[stackInd]=(i-stackInd)
            stack.append([t,i])
        return res
        
 #my solution which the time limit exceeded
 class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=len(temperatures)
        res=[0]*l
        for i in range(l-1):
            temp=1
            for j in temperatures[i+1:]:
                if temperatures[i]<j:
                    res[i]=temp
                    temp=0
                    break
                else:
                    temp+=1
        return res
