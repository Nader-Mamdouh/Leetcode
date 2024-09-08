class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Calculate the length of the linked list
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next  
        base_size = length // k
        larger_parts_count = length % k
        result = []
        cur = head
        
        for i in range(k):
            part_head = cur
            part_size = base_size + (1 if i < larger_parts_count else 0)
            for j in range(part_size - 1):
                if cur:
                    cur = cur.next
            if cur:
                next_part = cur.next
                cur.next = None
                cur = next_part     
            result.append(part_head)
        
        return result
