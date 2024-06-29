import pytest
from typing import List

class CanJump:
    def canJump(self, nums: List[int]) -> bool:
        n= len(nums)
        lp = n-1
        for i in range(n-1, -1, -1):
            if nums[i] + i <= lp:
                lp = i
        return lp == 0
    

