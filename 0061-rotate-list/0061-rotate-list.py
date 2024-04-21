# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def get_length(self, head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        length = self.get_length(head)
        k = k % length    
        
        if k == 0:
            return head
        
        current = head
        for _ in range(length - k - 1):
            current = current.next
        
        new_head = current.next
        current.next = None
        
        current = new_head
        while current.next:
            current = current.next
        
        current.next = head
        
        return new_head
