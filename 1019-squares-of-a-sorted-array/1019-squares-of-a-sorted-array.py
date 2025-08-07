class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # brute force: square the list and sort it
        # optimal approach ~ two pointers

        # square up the array, and then use two pointers to reverse sort it
        # return the reverse of the answer array

        n = len(nums)

        for i in range(n):
            nums[i] = nums[i] ** 2
        
        i , j = 0, n-1
        ans = []
        while i <= j:
            if nums[i] >= nums[j]:
                ans.append(nums[i])
                i += 1
            else:
                ans.append(nums[j])
                j -= 1
        
        return ans[::-1]
