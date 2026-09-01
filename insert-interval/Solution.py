class Solution(object):
    def insert(self, ii, new):
        ans = []
        i = 0
        while i < len(ii) and ii[i][1] < new[0]:
            ans.append(ii[i])
            i += 1
        
        while i < len(ii) and ii[i][0] <= new[1]:
            new = [min(new[0], ii[i][0]), max(new[1], ii[i][1])]
            i += 1
        ans.append(new)
        
        while i < len(ii):
            ans.append(ii[i])
            i += 1
        
        return ans