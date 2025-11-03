class Solution:
    def next_greater(self, nums : List[int]) -> List[dict]:
        stk=[]
        n = len(nums)
        # storing both value and index
        ans = {}
        for i in range(n-1, -1, -1):
            curr = nums[i]
            while stk and stk[-1][0] <= curr:
                stk.pop()
            if stk:
                ans[curr] =  stk[-1][0]
            stk.append((curr, i))
        print(ans)
        return ans
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = self.next_greater(nums2)
        n = len(nums1)
        ans = [-1] * n
        for i in range(n):
            if nums1[i] in arr:
                ans[i] = arr[nums1[i]]
        return ans
        