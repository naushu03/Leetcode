class Solution:
    def findGCD(self, nums: list[int]) -> int:
        s,l=min(nums),max(nums)
        for i in range(s,0,-1):
            if s%i==0 and l%i==0:
                return i
                break
