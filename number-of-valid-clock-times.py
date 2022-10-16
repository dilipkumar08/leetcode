class Solution:
    def countTime(self, time: str) -> int:
        m,n=time.split(":")
        res1=0
        if m[0]=="?":
            if m[1]=="?":
                res1=24
            else:
                if int(m[1])>=4:
                    res1=2
                else:
                    res1=3
        else:
            if m[1]=="?":
                if int(m[0])>1:
                    res1=4
                else:
                    res1=10
        res2=0
        if n[0]=='?':
            if n[1]=="?":
                res2=60
            else:
                res2=6
        else:
            if n[1]=="?":
                res2=10
        if res1==0 and res2!=0:
            return res2
        elif res2==0 and res1!=0:
            return res1
        elif res1==0 and res2==0:
            return 1
        else:
            return res1*res2
