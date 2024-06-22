'''
Longest Substring Without Repeating Characters
Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
Example 3:
    Input: s = "pwwkew" 
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class LLS_woRepetingCaharcter:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        dictCharPosition= {}
        p1, p2, maxlength =  0, 0, 0
        while p2 < n:
            if s[p2] in dictCharPosition:
                 p1= max(p1, dictCharPosition[s[p2]])
            dictCharPosition[s[p2]]= p2+1
            maxlength= max(maxlength, p2-p1+1)
            p2 +=1 

        return maxlength
    
if __name__ == "__main__":
    s = "dvdf"
    obj= LLS_woRepetingCaharcter()
    print(obj.lengthOfLongestSubstring(s))
