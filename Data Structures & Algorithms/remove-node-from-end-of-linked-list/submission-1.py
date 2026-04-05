# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)

        def dfs(curr):
            nonlocal n

            if curr.next:
                dfs(curr.next)

            n -= 1
            if n == -1:
                curr.next = curr.next.next
        dfs(dummy)
        return dummy.next
                

        