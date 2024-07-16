import pytest
from src.strings.merge_Strings_Alternately_1768 import MergeStringsAlternately
from src.strings.greatest_Common_Divisor_of_Strings_1071 import Greatest_Common_Divisor_of_Strings

class TestMergeStringsAlternately:
    @pytest.mark.parametrize("word1, word2, expected",{
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd")
    })
    def test_mergeStringsAlternately(self, word1, word2, expected):
        obT= MergeStringsAlternately()
        assert obT.mergeAlternately(word1, word2) == expected
        
class  Test_Greatest_Common_Divisor_of_Strings:
    @pytest.mark.parametrize("str1, str2, expected",{
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("ABABABT", "ABAB", ""),
        ("LEET", "CODE", "")
    })
    def test_gcd(self, str1, str2, expected):
        obT= Greatest_Common_Divisor_of_Strings()
        assert obT.gcdOfStrings(str1, str2) == expected

from src.strings.reverse_Words_in_a_String_151 import Reverse_Words_in_a_String_151        
class Test_Reverse_Words_in_a_String_151:
    @pytest.fixture
    def reverser(self):
        return Reverse_Words_in_a_String_151()
    
    COMMON_ARG= pytest.mark.parametrize("input, output",[
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a")
    ])
    @COMMON_ARG
    def test_reverseWords(self, reverser, input, output):
        assert reverser.reverseWords(input) == output
    
    @COMMON_ARG
    def test_reverseWords_discreate(self, reverser, input, output):
        assert reverser.reverseWords_discreate(input) == output
        
        
from src.strings.valid_Palindrome_125 import Solution_isPalindrome
class Test_Solution_isPalindrome:
    @pytest.mark.parametrize("s, expected", [
        ("A man, a plan, a canal: Panama", True),
        (" ", True),
        ("race a car", False)
    ])
    def test_isPalindrome(self, s, expected):
        tobj= Solution_isPalindrome()
        assert tobj.isPalindrome(s) == expected
