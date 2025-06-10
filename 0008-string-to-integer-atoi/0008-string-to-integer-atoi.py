class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        print(s)
        n = len(s)
        if n <=0:
            return 0
        sign = 1
        temp = "0"
        sign = -1 if s[0] == '-' else 1
        for i in range(n):
            if (i==0) and (s[i] =='-' or s[i] == '+'):
                continue 
            elif not s[i].isdigit():
                break
            elif s[i].isdigit():
                temp += s[i]
        
        res = sign * int(temp)
        if res < -2 ** 31:
            res =  -2 ** 31
        if res > (2 ** 31) - 1:
            res = (2 ** 31) - 1
        return res
        