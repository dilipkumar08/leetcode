class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res=['0']
        if k==1 and len(num)==1:
            return '0'
        else:
            for i in num:
            
                while(res and i<res[-1]   and k!=0):
                    res.pop()
                    k-=1
                res.append(i)
            
            while res and res[0]=='0':
                res.pop(0)
            res=''.join(res[:len(res)-k])
            return  str(res) if res else '0'
