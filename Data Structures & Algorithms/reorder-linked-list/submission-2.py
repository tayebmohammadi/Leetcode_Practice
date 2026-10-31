# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        left, right = head, head

        while right and right.next:
            left = left.next
            right = right.next.next

        sec_half = left.next
        left.next = None


        prev = None
        curr = sec_half
        while curr:
            nxt =  curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first_half = head
        sec_half = prev

        while sec_half:
            n1, n2 = first_half.next, sec_half.next

            first_half.next = sec_half
            sec_half.next = n1

            first_half = n1
            sec_half = n2
        




        

        































        # left , right = head, head

        # while right and right.next:
        #     left = left.next
        #     right= right.next.next

        # sec_half = left.next
        # left.next = None

        # curr = sec_half
        # prev = None

        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt

        # sec_half = prev
        # fir_half = head

        # while sec_half:

        #     t1 = fir_half.next
        #     t2 = sec_half.next

        #     fir_half.next = sec_half
        #     sec_half.next = t1

        #     fir_half = t1
        #     sec_half = t2
            










        