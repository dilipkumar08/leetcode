class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        n=len(s)//2
        a=s[:n]
        b=s[n:]
        A,B=0,0
        for i in range(n):
            if a[i]=="a":
                A+=1
            elif a[i]=="e":
                A+=1
            elif a[i]=="i":
                A+=1
            elif a[i]=="o":
                A+=1
            elif a[i]=="u":
                A+=1
            if b[i]=="a":
                B+=1
            elif b[i]=="e":
                B+=1
            elif b[i]=="i":
                B+=1
            elif b[i]=="o":
                B+=1
            elif b[i]=="u":
                B+=1
        return A==B
                
