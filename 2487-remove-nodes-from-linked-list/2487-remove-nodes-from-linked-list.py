# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_linked_list(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        head = self.reverse_linked_list(head)
        cur = head
        prev = None
        while cur:
            if not prev:
                prev = cur
                cur = cur.next
            else:
                if cur.val < prev.val:
                    prev.next = cur.next
                else:
                    prev = cur
                cur = cur.next

        head = self.reverse_linked_list(head)
        
        return head
