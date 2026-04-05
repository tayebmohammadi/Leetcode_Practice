# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        left , right = head, head

        while right and right.next:
            left = left.next
            right= right.next.next

        sec_half = left.next
        left.next = None

        curr = sec_half
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        sec_half = prev
        fir_half = head

        while sec_half:

            t1 = fir_half.next
            t2 = sec_half.next

            fir_half.next = sec_half
            sec_half.next = t1

            fir_half = t1
            sec_half = t2
            










        