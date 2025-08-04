class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            summ = nums[i] + nums[j]
            if summ == target:
                return [i+1, j+1]
            elif summ > target:
                j-=1
            else:
                i += 1
        return [-1, -1]