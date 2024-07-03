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
        
