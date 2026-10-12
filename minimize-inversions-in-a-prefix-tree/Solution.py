from bisect import bisect_left

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_index = -1
        self.subtree_positions = []

class Solution:
    def minInversions(self, words: list[str], target: list[int]) -> int:
        pos = {val: i for i, val in enumerate(target)}
        root = TrieNode()
        for i, word in enumerate(words):
            curr = root
            for char in word:
                curr = curr.children.setdefault(char, TrieNode())
            curr.word_index = i

        def populate(node):
            if node.word_index != -1:
                node.subtree_positions.append(pos[node.word_index])
            for child in node.children.values():
                populate(child)
                node.subtree_positions.extend(child.subtree_positions)
            node.subtree_positions.sort()

        populate(root)
        total = 0

        def solve(node):
            nonlocal total
            if node.word_index != -1:
                total += bisect_left(node.subtree_positions, pos[node.word_index])
            
            ch = list(node.children.values())
            k = len(ch)
            if k > 1:
                sub_lists = [c.subtree_positions for c in ch]
                cost = [[0] * k for _ in range(k)]
                for i in range(k):
                    si = sub_lists[i]
                    for j in range(k):
                        if i != j:
                            sj = sub_lists[j]
                            q = s = 0
                            for x in si:
                                while q < len(sj) and sj[q] < x:
                                    q += 1
                                s += q
                            cost[i][j] = s

                dp = [float("inf")] * (1 << k)
                dp[0] = 0
                for mask in range(1 << k):
                    if dp[mask] == float("inf"):
                        continue
                    for i in range(k):
                        if not (mask & (1 << i)):
                            add = sum(cost[j][i] for j in range(k) if mask & (1 << j))
                            nxt = mask | (1 << i)
                            if dp[mask] + add < dp[nxt]:
                                dp[nxt] = dp[mask] + add
                total += dp[(1 << k) - 1]

            for child in ch:
                solve(child)

        solve(root)
        return total