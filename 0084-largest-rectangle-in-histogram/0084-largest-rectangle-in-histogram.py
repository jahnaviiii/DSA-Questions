class Solution:
    def next_smaller(self, heights : List[int]) -> List[int]:
        n = len(heights)
        ans = [n] * n
        print(ans)
        stk = []
        for i in range(n-1, -1, -1):
            curr = heights[i]
            while stk and heights[stk[-1]] >= curr:
                stk.pop()
            if stk:
                ans[i] = stk[-1]
            stk.append(i)
        return ans

    def prev_smaller(self, heights : List[int]) -> List[int]:
        n = len(heights)
        ans = [-1] * n
        stk = []
        for i in range(n):
            curr = heights[i]
            while stk and heights[stk[-1]] >= curr:
                stk.pop()
            if stk:
                ans[i] = stk[-1]
            stk.append(i)
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        prev_smaller= self.prev_smaller(heights)
        next_smaller = self.next_smaller(heights)
        for i in range(n):
            currHeight = heights[i]
            width = next_smaller[i] - prev_smaller[i] - 1
            area = max(area, currHeight * width)
        return area
        