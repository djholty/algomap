
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelset = set([j for j in jewels])
        c = 0
        for s in stones:
            if s in jewelset:
                c += 1
        return c
