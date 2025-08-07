class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        delta = (sumB - sumA) // 2

        bobSet = set(bobSizes)

        for x in aliceSizes:
            if delta + x in bobSet:
                return [x, delta + x] 
        
        return [-1, -1]
        