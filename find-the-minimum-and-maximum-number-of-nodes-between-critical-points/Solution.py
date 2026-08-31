# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        ind = 1
        
        fc = -1
        pc = -1
        mini = float('inf')
        
        while curr.next:
            fa = curr.val > prev.val and curr.val > curr.next.val
            fi = curr.val < prev.val and curr.val < curr.next.val
            
            if fa or fi:
                if fc == -1:
                    fc = ind
                else:
                    mini = min(mini, ind - pc)
                
                pc = ind
            
            prev = curr
            curr = curr.next
            ind += 1
            
        if pc == fc:
            return [-1, -1]
            
        maxi = pc - fc
        return [mini, maxi]