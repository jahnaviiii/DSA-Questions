class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        sum = 0
        for x in operations:
            if x == "+":
                stk.append(stk[-1] + stk[-2])
                sum += stk[-1]
            elif x == "D":
                stk.append(stk[-1] * 2)
                sum += stk[-1]
            elif x == "C":
                sum -= stk.pop()
            else:
                stk.append(int(x))
                sum += stk[-1]
        return sum