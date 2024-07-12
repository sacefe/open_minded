class RomanToIntSolution:
    def romanToInt(self, s: str) -> int:
        romanDict= {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000, 
        }
        
        i=0
        res= 0
        while i < len(s):
            if i+1 < len(s) and romanDict[s[i]] < romanDict[s[i+1]]:
                res += romanDict[s[i+1]] - romanDict[s[i]]
                i +=2
            else:
                res += romanDict[s[i]]
                i +=1
        return res