class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = len(word1)
        q = len(word2)
        i=0
        j=0
        merged = []

        while(i < p or j < q):
            if i < p:
                merged += word1[i]
                i +=1
            if j < q:
                merged += word2[j]
                j += 1
        return "".join(merged)  
              