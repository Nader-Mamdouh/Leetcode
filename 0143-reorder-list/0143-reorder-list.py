# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        # Step 2: Reverse the second half
        prev = None
        curr = second_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        second_half = prev

        # Step 3: Merge the two halves alternately
        first_curr, second_curr = head, second_half
        while second_curr:
            first_next = first_curr.next
            second_next = second_curr.next

            first_curr.next = second_curr
            second_curr.next = first_next

            first_curr = first_next
            second_curr = second_next
