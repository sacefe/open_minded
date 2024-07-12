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

 
