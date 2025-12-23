class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2 ** 31 - 1
        mult = 1
        if x < 0:
            x = -x
            mult = -1

        result = 0
        while x > 0:
            result *= 10
            result += x % 10
            if result > MAX_INT:
                return 0
            x //= 10

        return result * mult
    
print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))