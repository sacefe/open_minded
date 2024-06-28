import pytest
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n= len(nums)
        lp = n-1
        for i in range(n-1, -1, -1):
            if nums[i] + i <= lp:
                lp = i
        return lp == 0
    


class Test():  
    def test_canJump(self):
        testcases={
            "t1": ([2,3,1,1,4], True),
            "t2": ([3,2,1,0,4], False)
        }
        objT= Solution()
        for _, tcase in testcases.items():
            assert objT.canJump(tcase[0]) == tcase[1]

pytest.main(['-v'])