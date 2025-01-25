class Solution:
  class Solution:
    def reverseBitsVer1(self, n: int) -> int:
        ans = 0
        for i in range(32):
            rBit = n%2
            n = n//2
            ans += rBit*(2**(31-i))
        return ans

class WithInternetKnowlege:
    def reverseBitsVer2(self, n: int) -> int:
        ans = 0
        for i in range(32):
            rBit = n & 1
            n >>= 1
            ans <<=1
            ans += rBit
        return ans

class FirstStepOptimization:
    def reverseBitsFinalVer(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans <<=1
            ans += (n & 1)
            n >>= 1
        return ans
