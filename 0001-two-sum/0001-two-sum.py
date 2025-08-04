class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map = {}

        # for ind, val in enumerate(nums):
        #     diff = target - val

        #     if diff in hash_map:
        #         return [ind, hash_map[diff]]
        #     hash_map[val] = ind
        # return [-1, -1]
        my_list = nums
        for i in range(len(nums)):
            my_list[i] = [nums[i], i]
        my_list.sort()
        i, j = 0, len(my_list) - 1
        while i < j:
            summ = my_list[i][0] + my_list[j][0]
            if summ == target:
                return [my_list[i][1], my_list[j][1]]
            elif summ > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]        