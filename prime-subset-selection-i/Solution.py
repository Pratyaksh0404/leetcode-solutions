class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        if n < 2 or s < 2:
            return []
        
        sieve = bytearray([1]) * (n + 1)
        sieve[0] = sieve[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
        
        ans = []
        curr = 0
        for i in range(2, n + 1):
            if sieve[i]:
                if curr + i <= s:
                    curr += i
                    ans.append(i)
                else:
                    break
                    
        return ans