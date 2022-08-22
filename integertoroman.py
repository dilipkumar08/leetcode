class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]    
        l=len(values)     
        result = ""
        while num != 0:
            for i in range(l):
                if num >= values[i]:
                    result += romans[i]
                    num -= values[i]
                    break
        return result
