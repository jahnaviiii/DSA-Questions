#User function Template for python3


class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        summ = 0
        temp = n
        while temp != 0:
            rem = temp % 10
            summ += rem
            temp = temp // 10
        
        s = str(summ)
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
        # 1 77 1