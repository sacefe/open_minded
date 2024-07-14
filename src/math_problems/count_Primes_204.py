from math import sqrt
class Solution_CountPrimes:
    def countPrimes(self, n: int) -> int:
        #primes 2,3,5,7,11..
        #primes of n are until sqroot(n)+1 plus its multiples
        primesTable= [False, False] + [True] * (n - 2)
        for p in range(2, int(sqrt(n))+1 , 1):
            for i in range(p*p, n, p):
                primesTable[i]= False

        primes= sum(primesTable)
        
        return primes