class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            dig = x % 10
            x //= 10

            # overflow check BEFORE update
            if rev > (2**31 - 1) // 10 or (
                rev == (2**31 - 1) // 10 and dig > 7
            ):
                return 0

            rev = rev * 10 + dig

        return rev * sign


            


            