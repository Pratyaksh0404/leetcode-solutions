class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        def solve(k):
            for i in range(0,n,k):
                sub = nums[i:i+k]
                tar = s[i:i+k]
                if sorted(sub)!= tar:
                    return False

                if k>1:
                    d = 0
                    for j in range(k):
                        if sub[j]>sub[(j+1)%k]:
                            d += 1
                    if d>1:
                        return False
            return True
            
        ans = 0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                if solve(i):
                    ans += i
                o = n//i
                if o != i:
                    if solve(o):
                        ans += o
            

        return ans