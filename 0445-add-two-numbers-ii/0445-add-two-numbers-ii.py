class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    def reverse(self, head):
        p, q = head, None
        
        while p:
            on = p.next  
            p.next = q   
            q = p
            p = on
            
        return q
    
    def addTwoNumbers(self, head1, head2):
        p = self.reverse(head1)
        q = self.reverse(head2)
        
        head = last = ListNode(-1)  
        
        carry = 0
        while p or q:
            d = (p.val if p else 0) + (q.val if q else 0) + carry
            
            temp = ListNode(d % 10)
            last.next = temp
            last = temp
            
            carry = d // 10
            
            if p:
                p = p.next
            if q:
                q = q.next
        
        if carry != 0:
            temp = ListNode(carry)
            last.next = temp
            last = temp
        
        head = head.next  
        head = self.reverse(head)
        
        return head
