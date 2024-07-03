class MergeStringsAlternately:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1l= len(word1)
        w2l= len(word2)
        p=0
        res=[] #* (w1l+w2l) 
        while p<w1l or p<w2l:
            if p<w1l: 
                res.append(word1[p])
            if p<w2l:
                res.append(word2[p])
            p +=1

        
        return ''.join(res)
