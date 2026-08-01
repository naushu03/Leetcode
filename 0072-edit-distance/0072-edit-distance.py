class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def check(i,j):
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if word1[i]==word2[j]:
                return check(i+1,j+1)
            if word1[i]!=word2[j]:
                ins=1+check(i,j+1)
            if word1[i]!=word2[j]:
                dele=1+check(i+1,j)
            if word1[i]!=word2[j]:
                upd=1+check(i+1,j+1)
            return min(ins,dele,upd)

        return check(0,0)