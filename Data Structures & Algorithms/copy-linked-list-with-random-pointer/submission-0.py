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
        curr = head
        copyToNew = {None: None}
        
        while curr:
            copy = Node(curr.val)
            copyToNew[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = copyToNew[curr]
            copy.next = copyToNew[curr.next]
            copy.random = copyToNew[curr.random]
            curr = curr.next
        return copyToNew[head]    

