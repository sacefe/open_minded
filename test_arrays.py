# from unittest import TestCase
import pytest
from arrays.container_With_Most_Water_11 import *
from arrays.longest_Substring_wo_Repeating_Characters_3 import *
from arrays.sum3_15 import *

class Test_container_With_Most_Water(): #(TestCase): 
    def test_always_passes(self):
        height= [1,8,6,2,5,4,8,3,7]
        obj= Water_Containers()
        assert obj.maxArea(height) == 49
        

class Test_lengthOfLongestSubstring():  #(TestCase): 
    def test_always_passes(self):
        s = "abcabcbb"
        obj=  LLS_woRepetingCaharcter()
        assert obj.lengthOfLongestSubstring(s) == 3

        s = "bbbbb" 
        assert obj.lengthOfLongestSubstring(s) == 1

        s = "pwwkew" 
        assert obj.lengthOfLongestSubstring(s) == 3

        s = "abba" 
        assert obj.lengthOfLongestSubstring(s) == 2

        s = "dvdf"
        assert obj.lengthOfLongestSubstring(s) == 3

        s = " "
        assert obj.lengthOfLongestSubstring(s) == 1

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