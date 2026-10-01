# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        
        while head:
            temp.append(head.val)
            head = head.next

        dummy = ListNode(0)
        curr = dummy
        temp.sort()

        for i in temp:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next
        