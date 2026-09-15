# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sa = ['A']
        sb = ['B']

        while headA or headB:
            if headA:
                sa.append(headA)
                headA = headA.next

            if headB:
                sb.append(headB)
                headB = headB.next

        prev = None
        while sa and sb:
            nodeA = sa.pop(-1)
            nodeB = sb.pop(-1)

            if nodeA != nodeB:
                return prev

            prev = nodeA