import pytest
from src.strings.merge_Strings_Alternately_1768 import MergeStringsAlternately

class TestMergeStringsAlternately:
    @pytest.mark.parametrize("word1, word2, expected",{
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd")
    })
    def test_mergeStringsAlternately(self, word1, word2, expected):
        obT= MergeStringsAlternately()
        assert obT.mergeAlternately(word1, word2) == expected