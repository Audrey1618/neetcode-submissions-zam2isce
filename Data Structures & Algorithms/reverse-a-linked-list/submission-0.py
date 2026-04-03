# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None

        curr = head #0
        prev = None
        nxt = head.next #1
    
        while nxt:
            temp = nxt.next #2
            curr.next = prev #0 -> None
            nxt.next = curr # 1 -> 0 -> None
            
            prev = curr #0
            curr = nxt #1
            nxt = temp #2

        return curr
    
    




       




