class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            # since nums is sorted, if nums[i] is +ve, the sum of further elems would always be > 0.
            if nums[i] > 0:
                break
            
            #if the starting numbers are same, we just move the i pointer forward [-1, -1, -1, 0, 1, 1...]
            elif i > 0 and nums[i] == nums[i-1]:
                i += 1
            else:
                low = i + 1
                high = n - 1
                while(low < high):
                    summ = nums[i] + nums[low] + nums[high]
                    if summ == 0:
                        ans.append([nums[i], nums[low], nums[high]])
                        # move the pointers to next elems
                        low, high = low+1, high-1

                        # move the pointers to next diff elems
                        # keep on incrementing left until we get an elem > than current elem

                        while low < high and nums[low] == nums[low-1]:
                            low += 1
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
                    elif summ > 0:
                        high -= 1
                    else:
                        low += 1
        return ans
        