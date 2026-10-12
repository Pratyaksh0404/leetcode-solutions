class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bits = [0] * 31
        MOD = int(1e9 + 7)
        ans = 0

        for n in nums:
            while n:
                bit = n & -n
                n -= bit
                bits[bit.bit_length()-1] += 1
        
        while k:
            curr = 0

            for i in range(30, -1, -1):
                curr <<= 1
                if bits[i]:
                    curr |= 1
                    bits[i] -= 1
                    
            ans = (ans + (curr ** 2) % MOD) % MOD
            k -= 1
        
        return ans
