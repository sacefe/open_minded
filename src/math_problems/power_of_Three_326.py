
class Solution_isPowerOfThree:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: 
            return False
        
        while n%3 == 0:
            n /=3
 
        'True if n==1 else False '
        return  n==1
        