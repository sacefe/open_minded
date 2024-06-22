from unittest import TestCase
from arrays.container_With_Most_Water_11 import *
from arrays.longest_Substring_wo_Repeating_Characters import *


class Test_container_With_Most_Water(TestCase): 
    def test_always_passes(self):
        height= [1,8,6,2,5,4,8,3,7]
        obj= Water_Containers()
        assert obj.maxArea(height) == 49
        

class Test_lengthOfLongestSubstring(TestCase):
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