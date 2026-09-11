class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = {}
        for d in digits:
            freq[d] = freq.get(d, 0) + 1
            
        count = 0
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            req = {}
            req[d1] = req.get(d1, 0) + 1
            req[d2] = req.get(d2, 0) + 1
            req[d3] = req.get(d3, 0) + 1
            
            if all(freq.get(d, 0) >= req[d] for d in req):
                count += 1
                
        return count