class Reverse_Words_in_a_String_151:
    def reverseWords(self, s: str) -> str:   
        revArr=  reversed(s.split())
        return " ".join(revArr)
    
    def reverseWords_discreate(self, s: str) -> str:
        arrstr= s.split(" ")
        arrstr=[word for word in arrstr if word!='']
        res= [] 
        for i in range(len(arrstr)-1, -1, -1 ):
            res.append(arrstr[i])
        
        return " ".join(res)
            