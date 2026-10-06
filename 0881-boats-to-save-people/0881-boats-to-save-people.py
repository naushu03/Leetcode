class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        c=0
        i,j=0,len(people)-1
        while i<=j:
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
            c+=1
        return c
        