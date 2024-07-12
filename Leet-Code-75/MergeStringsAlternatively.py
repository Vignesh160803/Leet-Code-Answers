class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lptr=0
        rptr=0
        n=len(word1)
        m=len(word2)
        res=""
        while lptr<n and rptr<m:
            res+=word1[lptr]+word2[rptr]
            lptr+=1
            rptr+=1
        while lptr<n:
            res+=word1[lptr]
            lptr+=1
        while rptr<m:
            res+=word2[rptr]
            rptr+=1

        return res
    