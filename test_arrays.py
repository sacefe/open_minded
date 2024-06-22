from unittest import TestCase
from arrays.container_With_Most_Water_11 import *


class Test_container_With_Most_Water(TestCase): 
    def test_always_passes(self):
        height= [1,8,6,2,5,4,8,3,7]
        obj= Solution()
        assert obj.maxArea(height) == 49      

