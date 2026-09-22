class SegmentTree:
    def __init__(self, data, k):
        self.n = len(data)
        self.k = k
        self.count = [[0] * k for _ in range(4 * self.n)]
        self.prod = [1] * (4 * self.n)
        self.build(data, 0, 0, self.n-1)

    def _merge(self, tree_idx, left_child, right_child):
        self.prod[tree_idx] = (self.prod[left_child] * self.prod[right_child]) % self.k
        k = self.k
        c_left = self.count[left_child]
        c_right = self.count[right_child]
        p_left = self.prod[left_child]
        
        c = [c_left[r] for r in range(k)]
        for r in range(k):
            if c_right[r]:
                new_r = (p_left * r) % k
                c[new_r] += c_right[r]
        self.count[tree_idx] = c

    def build(self, data, tree_idx, l, r):
        if l == r:
            val = data[l] % self.k
            self.prod[tree_idx] = val
            self.count[tree_idx] = [0] * self.k
            self.count[tree_idx][val] = 1
            return
        mid = (l + r) // 2
        left_child = 2 * tree_idx + 1
        right_child = 2 * tree_idx + 2
        self.build(data, left_child, l, mid)
        self.build(data, right_child, mid + 1, r)
        self._merge(tree_idx, left_child, right_child)

    def update(self, tree_idx, l, r, idx, val):
        if l == r:
            v = val % self.k
            self.prod[tree_idx] = v
            self.count[tree_idx] = [0] * self.k
            self.count[tree_idx][v] = 1
            return
        mid = (l + r) // 2
        left_child = 2 * tree_idx + 1
        right_child = 2 * tree_idx + 2
        if idx <= mid:
            self.update(left_child, l, mid, idx, val)
        else:
            self.update(right_child, mid + 1, r, idx, val)
        self._merge(tree_idx, left_child, right_child)

    def query(self, tree_idx, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.prod[tree_idx], self.count[tree_idx]
        
        mid = (l + r) // 2
        left_child = 2 * tree_idx + 1
        right_child = 2 * tree_idx + 2
        
        if qr <= mid:
            return self.query(left_child, l, mid, ql, qr)
        if ql > mid:
            return self.query(right_child, mid + 1, r, ql, qr)
            
        p_left, c_left = self.query(left_child, l, mid, ql, qr)
        p_right, c_right = self.query(right_child, mid + 1, r, ql, qr)
        
        tot_prod = (p_left * p_right) % self.k
        k = self.k
        tot_count = [c_left[rem] for rem in range(k)]
        for rem in range(k):
            if c_right[rem]:
                new_rem = (p_left * rem) % k
                tot_count[new_rem] += c_right[rem]
                
        return tot_prod, tot_count


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(nums, k)
        ans = []
        
        for idx, val, start, target_x in queries:
            st.update(0, 0, n - 1, idx, val)
            _, count_arr = st.query(0, 0, n - 1, start, n - 1)
            ans.append(count_arr[target_x])
            
        return ans