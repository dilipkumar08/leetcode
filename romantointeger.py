class Solution:
    def romanToInt(self, s: str) -> int:
        i=0
        answer = 0
        l=len(s)
        nums =	{"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        
        subs = {"IV": 4,"IX": 9,"XL": 40,"XC": 90,"CD": 400,"CM": 900}
        
        while i< l:
            if s[i:i+2] in subs:
                answer += subs[s[i:i+2]]
                i+= 2
            else:
                answer += nums[s[i]]
                i += 1
                
        return answer
