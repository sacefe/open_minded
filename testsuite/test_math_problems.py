import pytest

from src.math_problems.pass_the_Pillow_2582 import Pass_the_Pillow

class Test_PassPillow:
    @pytest.fixture
    def tobj(self):
        return Pass_the_Pillow()
    @pytest.mark.parametrize("n, time, expected",[
        (4 , 5, 2),
        (3, 2, 3)
    ])
    def test_passpillow(self, tobj, n, time, expected):
        tobj= Pass_the_Pillow()
        assert tobj.passThePillow(n, time) == expected

from src.math_problems.roman_to_Integer_13 import RomanToIntSolution
class Test_romanToInt():
    @pytest.mark.parametrize("s, expected",{
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994)
    })
    def test_romantoInt(self, s, expected):
        tObj= RomanToIntSolution()
        myRomanInt= tObj.romanToInt(s) 
        assert myRomanInt == expected

from src.math_problems.power_of_Three_326 import Solution_isPowerOfThree
class Test_isPowerOfThree(): 
    @pytest.mark.parametrize("n, expected", [
        (27, True),
        (9, True),
        (0, False),
        (-1, False),
        (81, True)
    ])
    def tes_isPowTree(self, n, expected):
        tObj= Solution_isPowerOfThree()
        assert tObj.isPowerOfThree(n) == expected
