class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search soln
        n = len(nums)
        l, r = 0 , n - 1

        ans = float('inf')

        while l<=r:
            mid = (l + r) // 2
            # identify the sorted half and assign min element and eliminate the sorted half
            
            # left sorted:
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            elif nums[mid] <= nums[r]:
                ans = min(nums[mid], ans)
                r = mid - 1
        
        return ans
        