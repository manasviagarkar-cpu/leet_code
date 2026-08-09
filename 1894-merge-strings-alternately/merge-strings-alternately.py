class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p ,q  = len(word1) , len(word2)
        i , j = 0 , 0
       
        merged = []

        while(i < p or j < q):
            if i < p:
                merged += word1[i]
                i +=1
            if j < q:
                merged += word2[j]
                j += 1
        return "".join(merged)  
              