# from unittest import TestCase
import pytest


from src.arrays.canJump import CanJump
class Test():  
    def test_canJump(self):
        testcases={
            "t1": ([2,3,1,1,4], True),
            "t2": ([3,2,1,0,4], False)
        }
        objT= CanJump()
        for _, tcase in testcases.items():
            assert objT.canJump(tcase[0]) == tcase[1]

from src.arrays.container_With_Most_Water_11 import Water_Containers
class Test_Water_Containers(): #(TestCase): 
    def test_always_passes(self):
        height= [1,8,6,2,5,4,8,3,7]
        obj= Water_Containers()
        assert obj.maxArea(height) == 49


from src.arrays.longest_Substring_wo_Repeating_Characters_3 import LLS_woRepetingCaharcter
class Test_lengthOfLongestSubpytesttring():  #(TestCase): 
    @pytest.mark.parametrize("s, expected",[
        ("abcabcbb", 3),
        ("bbbbb", 1 ),
        ("pwwkew", 3 ),
        ("abba", 2),
        ("dvdf", 3),
        (" ", 1)
    ])
    def test_always_passes(self, s,  expected):
        # s = "abcabcbb"
        obj=  LLS_woRepetingCaharcter()
        assert obj.lengthOfLongestSubstring(s) == expected
        # assert obj.lengthOfLongestSubstring(s) == 3

        # s = "bbbbb" 
        # assert obj.lengthOfLongestSubstring(s) == 1

        # s = "pwwkew" 
        # assert obj.lengthOfLongestSubstring(s) == 3

        # s = "abba" 
        # assert obj.lengthOfLongestSubstring(s) == 2

        # s = "dvdf"
        # assert obj.lengthOfLongestSubstring(s) == 3

        # s = " "
        # assert obj.lengthOfLongestSubstring(s) == 1


from src.arrays.multiply_Strings_43 import Multiply            
class Test_MultiplybyString():
    def test_always_passed(self):
        num1, num2 = "2", "3"
        obj = Multiply()
        obj.multiply(num1, num2) == "6"

        num1, num2 = "123", "456"
        obj.multiply(num1, num2) == "56088"


from src.arrays.next_permutation_31 import Next_Permutation
class Test_Next_permutation_31():
    @pytest.mark.parametrize("nums, expected",[
        ([1,2,3], [1,3,2]),
        ([3,2,1], [1,2,3] ),
        ([1,1,5], [1,5,1]),
    ])
    def test_alwats_passed(self, nums, expected):
        nums = [1,2,3]
        obj = Next_Permutation()
        obj.nextPermutation(nums)
        assert nums == [1,3,2]

from src.arrays.plusOne import Plus_One
class TestPlusOne():
    @pytest.fixture
    def sumatory(self):
        return Plus_One()
    
    @pytest.mark.parametrize("digits, expected",[
        ([9], [1,0]),
        ([4,3,2,1], [4,3,2,2]),
        ([1,2,3], [1,2,4])
    ])
    
    def test_plusOne(self, sumatory, digits, expected):
        output= sumatory.plusOne(digits)
        assert output == expected


from src.arrays.rotate_Image_48 import Rotate
class Test_Rotate():
    def test_matrix(self):
        obj2Test= Rotate()
        testcases= {
            "t1" : ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]), 
            "t2" : ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
        }
        for _, test in testcases.items():
            print(test)
            obj2Test.rotate(test[0])
            assert test[0] == test[1] 


from src.arrays.rotateArray import RotateArray
class TestRotate():
    @pytest.fixture
    def rotator(self):
        return RotateArray()
    @pytest.mark.parametrize("nums , k , expected",[
        ([-1,-100,3,99], 2, [3,99,-1,-100]),
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4])
    ])
    def test_rotate(self, rotator, nums , k , expected):
        res= rotator.rotate(nums, k)
        assert res == expected

        
from src.arrays.sum3_15 import *
class Test_sum3(): 
    def test_always_passed(self):
        obj= Sum3()

        nums = [-1,0,1,2,-1,-4]
        assert obj.threeSum(nums) == [[-1,-1,2],[-1,0,1]] or [[-1,0,1], [-1,-1,2]]
        # Explanation: 
        # nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        # nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        # nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        
        nums = [0,1,1]
        assert obj.threeSum(nums) == []
        # Explanation: The only possible triplet does not sum up to 0.

        nums = [0,0,0]
        assert obj.threeSum(nums) == [[0,0,0]]
        # Explanation: The only possible triplet sums up to 0.


# pytest.main(['-v'])