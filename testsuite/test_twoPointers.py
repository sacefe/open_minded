import pytest

from src.twoPointers.move_Zeroespy_283 import Move_Zeroes

class Test_Move_Zeroes():
    @pytest.mark.parametrize("nums, expected", [
        ([0,1,0,3,12], [1,3,12,0,0]),
        ([0], [0]),
        ([1,0,1], [1,1,0]),
    ])
    def test_moveZeros(self, nums, expected):
        tObj= Move_Zeroes()
        tObj.moveZeroes(nums) 
        assert nums == expected
    