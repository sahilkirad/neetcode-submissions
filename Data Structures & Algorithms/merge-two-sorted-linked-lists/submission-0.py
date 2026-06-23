# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        arr=ListNode()
        dupl=arr
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                dupl.next=ListNode(list1.val)
                
                list1=list1.next
            else:
                dupl.next=ListNode(list2.val)
             
                list2=list2.next
            dupl=dupl.next
        
        if list1:
            dupl.next=list1
        else:
            dupl.next=list2
        
        return arr.next

