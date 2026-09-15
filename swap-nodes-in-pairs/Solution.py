# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0, head)
        prev = d
        curr = head
        
        while curr and curr.next:
            np = curr.next.next
            second = curr.next
            
            second.next = curr     
            curr.next = np   
            prev.next = second      
            
            prev = curr
            curr = np
            
        return d.next