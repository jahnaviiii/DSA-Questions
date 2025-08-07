class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low , high = 0 , n-1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            
            # left half sorted
            elif nums[low] <= nums[mid]:
                # check if target lies in this range
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1 #reduce search space
                
                # if the element is not in left half, move left to the right half
                else:
                    low = mid + 1
            
            # right sorted
            elif nums[mid] <= nums[high]:
                # checking if target lies in this range
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
        return -1