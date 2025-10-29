class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            if char == '(' or char=='{' or char=='[':
                stk.append(char)
            elif char == ')':
                if len(stk) == 0 or stk[-1] != '(':
                    return False
                else:
                    stk.pop()
            elif char == ']':
                if len(stk) == 0 or stk[-1] != '[':
                    return False
                else:
                    stk.pop()
            elif char == '}':
                if len(stk) == 0 or stk[-1] != '{':
                    return False
                else:
                    stk.pop()
            
        
        # print(stk)
        return len(stk) == 0
        