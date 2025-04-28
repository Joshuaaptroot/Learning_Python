class Solution:
    def romanToInt(self, s: str) -> int:
        
        numerals = {
            "I": 1,
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
            }
        val = 0
        tempval = 0

        for i in s[::-1]:
            if tempval > numerals[i]:
                val -= numerals[i]
            else:
                val += numerals[i]
            
            tempval = numerals[i]

        return val
