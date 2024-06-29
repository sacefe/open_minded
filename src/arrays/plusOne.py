from typing import List
import pytest

class Plus_One:
    def plusOne(self, digits: List[int]) -> List[int]:

        intDigit = 0
        base = 1
        for i in range(len(digits)-1, -1, -1):
            intDigit += digits[i] * base
            base *=10
        intDigit +=1

        #ovreFlow
        n= len(digits)
        ov= intDigit /pow(10, n-1)
        if ov> 9:
            n += 1
        res=[0] * n

        for i in range(n):
            res[i] = intDigit//pow(10, n-1 - i)
            intDigit=  intDigit % pow(10, n-1 - i)   

        return res      
    

