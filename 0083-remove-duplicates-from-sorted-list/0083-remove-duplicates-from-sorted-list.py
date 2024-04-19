from collections import defaultdict

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = defaultdict(int)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head:
            dic[head.val] += 1
            if dic[head.val] > 1:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        
        return dummy.next
