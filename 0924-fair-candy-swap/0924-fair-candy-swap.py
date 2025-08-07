class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        delta = (sumB - sumA) // 2
        # if x is the candy to be removed from alice and y is the candy to be removed from bob
        # we just have to make sure that sumAlice - x + y == sumBob - y + x
        # after solving this, we get y = (sumBob - sumAlice)// 2 + x
        # we can consider delta = (sumBob - sumAlice) // 2

        bobSet = set(bobSizes)

        # for every candy in alice, if delta + candy exists in bob, then that can be exchanged
        # to maintain equal sum
        for x in aliceSizes:
            if delta + x in bobSet:
                return [x, delta + x] 
        
        return [-1, -1]
        