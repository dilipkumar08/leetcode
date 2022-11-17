# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        temp,i=1,n
        while True:
            m=(i+temp)//2
            g=guess(m)
            if g==1:
                temp=m+1
            elif g==-1:
                i=m
            else:
                return m
                
            
        
