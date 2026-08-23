# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverser(head, tail):

            prev = tail
            curr = head

            while curr != tail:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev, head

        dummy = ListNode(0, head)
        group_prev = dummy

        curr = head
        i = 1

        while curr:
            if i % k == 0:
                group_start = group_prev.next
                group_next = curr.next

                new_head, new_tail = reverser(
                    group_start,
                    group_next
                )

                group_prev.next = new_head
                group_prev = new_tail
                curr = group_next
            else:
                curr = curr.next

            i += 1

        return dummy.next




        