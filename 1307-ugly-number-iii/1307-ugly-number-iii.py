import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
                
        def lcm(a, b):
            return (a * b) // math.gcd(a, b)
        
        # function that returns the count of total values
        # that are divisible by a, b, c
        def func(mid, a, b, c):
            cnt = 0

            cnt += (mid // a)
            cnt += (mid // b)
            cnt += (mid // c)

            # subtracting duplicates
            # this subtracts everything not even one occurence remains
            # for an element that is divisible by a, b, and c
            cnt -= (mid // lcm(a, b))
            cnt -= (mid // lcm(b, c))
            cnt -= (mid // lcm(c, a))

            # add the elem which is divisible by all a, b, c
            cnt += (mid // lcm(a, lcm(b,c)))

            # print(cnt)
            return cnt
        
        low = 0
        high = 2 * (10 ** 9)
        print(func(49, 7, 7, 7))
        while low <= high:
            mid = low + (high - low) // 2
            cnt = func(mid, a, b, c)

            if (cnt == n) and (mid % a == 0 or mid % b == 0 or mid % c == 0):
                return int(mid)
            if cnt < n:
                low = mid + 1
            if cnt >= n:
                high = mid - 1
        
        return -1
