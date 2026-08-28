class Solution(object):
    def insert(self, ii, new):
        m = []
        i = 0

        while i < len(ii) and ii[i][1] < new[0]:
            m.append(ii[i])
            i += 1
        
        while i < len(ii) and ii[i][0] <= new[1]:
            new = [min(new[0], ii[i][0]), max(new[1], ii[i][1])]
            i += 1
        m.append(new)
        
        while i < len(ii):
            m.append(ii[i])
            i += 1
        
        return m