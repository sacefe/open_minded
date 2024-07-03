from math import gcd

class  Greatest_Common_Divisor_of_Strings:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # verify meet GDC rules
        if str1+str2 != str2+str1:
            return ""
        
        maxlength= gcd(len(str1), len(str2))
        div= str1[:maxlength]
        
        return div
        