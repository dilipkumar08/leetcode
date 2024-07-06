class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        start=1
        direction=1
        while time:
            if 1<start<n:
                start+=direction
                time-=1
            elif start==1:
                direction=1
                start+=1
                time-=1
            else:
                direction=-1
                start-=1
                time-=1
        return start

        
