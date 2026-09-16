class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(right**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, right + 1, p):
                    is_prime[i] = False
        
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        mini = float('inf')
        ans = [-1, -1]
        for i in range(len(primes) - 1):
            diff = primes[i+1] - primes[i]
            if diff < mini:
                mini = diff
                ans = [primes[i], primes[i+1]]
                
        return ans