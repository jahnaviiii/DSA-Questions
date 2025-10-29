class Solution:
    def isValid(self, s: str) -> bool:
        opening = '{(['
        map ={
            '}':"{",
            "]":"[",
            ")":"("
        }

        stk =[]
        for char in s:
            if char in opening:
                stk.append(char)
            else:
                if stk and map[char] == stk[-1]:
                    stk.pop()
                else:
                    return False
        
        return len(stk) == 0
        