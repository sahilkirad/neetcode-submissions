# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sl=head
        fa=head
        while sl is not None and fa is not None and fa.next is not None:
            sl=sl.next
            fa=fa.next.next # move twice
        
            if sl==fa:
                return True
        
        return False