class Solution(object):
    def canConstruct(self, rn, mag):
        st1, st2 = Counter(rn), Counter(mag)
        if st1 & st2 == st1:
            return True
        return False