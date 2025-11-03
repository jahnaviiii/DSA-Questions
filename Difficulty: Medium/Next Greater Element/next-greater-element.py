class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        stk = []
        ans = [-1] * n
        stk.append(arr[-1])
        
        for i in range(n-2, -1, -1):
            curr = arr[i]
            while stk and stk[-1] <= curr:
                stk.pop()
            if stk and stk[-1] > curr:
                ans[i] = stk[-1]
            stk.append(curr)
        return ans
        