# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy
    
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            tot = l1_val + l2_val + carry
            if tot >= 10:
                carry = tot // 10
                tot = tot % 10
            else:
                carry = 0

            node = ListNode(tot)
            curr.next = node
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry != 0:
            node = ListNode(carry)
            curr.next = node

        return dummy.next


