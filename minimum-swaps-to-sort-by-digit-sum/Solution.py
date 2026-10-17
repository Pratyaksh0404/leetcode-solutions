class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        n = len(nums)
        
        a = sorted(nums, key=lambda x: (digit_sum(x), x))
        
        b = {val: i for i, val in enumerate(nums)}
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or nums[i] == a[i]:
                continue
            
            size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                next_val = a[j]
                j = b[next_val]
                size += 1
            
            if size > 1:
                swaps += size - 1
        
        return swaps
