class Solution:
    def romanToInt(self, s: str) -> int:
        l=0
        answer = 0
        
        nums =	{
          "I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000,
            
        }
        
        subs = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        while l < len(s):
            if s[l:l+2] in subs:
                answer = answer + subs[s[l:l+2]]
                l += 2
            else:
                answer = answer + nums[s[l]]
                l += 1
                
        return answer
