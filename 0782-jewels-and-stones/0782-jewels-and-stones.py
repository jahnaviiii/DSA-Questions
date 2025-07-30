from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = defaultdict(int)

        for char in stones:
            d[char] += 1
        ans = 0
        for char in jewels:
            if d[char]:
                ans += d[char]
        return ans
        