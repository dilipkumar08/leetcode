class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squareroot=set()
        r=int(sqrt(c))+1

        for i in range(r):
            squareroot.add(i*i)
        
        for j in squareroot:
            target=c-j
            if target in squareroot:
                return True

        return False
