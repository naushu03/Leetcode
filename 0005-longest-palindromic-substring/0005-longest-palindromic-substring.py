class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        op=''
        for i in range(len(s)):
            x=check(i,i)
            y=check(i,i+1)
            op=max(op,x,y,key=len)
        return op