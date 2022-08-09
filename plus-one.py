#method1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b=''
        d=[]
        for i in digits:
            b=b+str(i)
            c=int(b)+1
        for i in str(c):
            d.append(int(i))
        return d
      
#method2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(x) for x in digits]
        digits = "".join(digits)
        digits = int(digits)+ 1
        digits = [int(y) for y in str(digits)]
        return digit
    
#method3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)-1
        digits[l]+=1
        while digits[l]==10 and l>0:
            digits[l]=0
            l-=1
            digits[l]+=1
        if digits[0]==10:
            digits[0]=0
            digits.insert(0,1)
        return digits
        
