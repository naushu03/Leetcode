class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        c=bin(start^goal).count('1')
        return c