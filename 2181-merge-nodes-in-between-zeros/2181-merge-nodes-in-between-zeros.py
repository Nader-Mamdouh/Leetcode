# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        summ = 0
        ans = []
        
        while cur:
            if cur.val == 0:
                ans.append(summ)
                summ = 0
            else:
                summ += cur.val
            cur = cur.next
        if not ans:
            return None
        
        new_head = ListNode(ans[0])
        current = new_head
        for value in ans[1:]:
            current.next = ListNode(value)
            current = current.next
        
        return new_head  
