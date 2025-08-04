class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join(x for x in s if x.isalnum()).lower()
        # return s == s[::-1]

        s = ''.join(x for x in s if x.isalnum()).lower()
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True