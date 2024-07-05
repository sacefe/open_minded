from typing import List

class KidsGreatestNumberCandies:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n= len(candies)
        
        candiesPlusExtra= [x + extraCandies for x in candies ]
        maxKidCandies= max(candies)
        
        result= [False if x<maxKidCandies else True for x in candiesPlusExtra]
        
        return result
    