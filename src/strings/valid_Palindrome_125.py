class Solution_isPalindrome:
    def isPalindrome(self, s: str) -> bool:
        filterChar= filter(lambda ch: ch.isalnum() ,s) 
        mapCharLower= map(lambda ch: ch.lower() ,filterChar)
        listStr= list(mapCharLower)
        reverseListStr= listStr[::-1]
        
        return listStr== reverseListStr