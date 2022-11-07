class Solution:
    def maximum69Number (self, num: int) -> int:
        res=""
        num=str(num)
        l=len(num)
        for i in range(l):
            if i+1<l:
                if num[i]=="6":
                    res+="9"+num[i+1:]
                    break
            if i+1==l:
                if num[i]=="6":
                    res+="9"
                    break
                
            res+=num[i]
        return int(res)
                
                
