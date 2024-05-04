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
        ans={None:None}
        cur =head
        while cur:
            value=Node(cur.val)
            ans[cur]=value
            cur=cur.next
        cur=head  
        while cur:
            copy = ans[cur]
            copy.next = ans[cur.next]
            copy.random = ans[cur.random]
            cur = cur.next  
        return ans[head]    