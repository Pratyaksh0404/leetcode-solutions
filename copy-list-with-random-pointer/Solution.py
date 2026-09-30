"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        o = {}
        
        curr = head
        while curr:
            o[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            o[curr].next = o.get(curr.next)
            o[curr].random = o.get(curr.random)
            curr = curr.next
            
        return o[head]