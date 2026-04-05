# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeList(l1, l2):

            dummy = ListNode(0)
            curr = dummy
            
            cur1, cur2 = l1, l2
            while cur1 and cur2:
                if cur1.val <= cur2.val:
                    curr.next = cur1
                    cur1 = cur1.next
                else:
                    curr.next = cur2
                    cur2 = cur2.next
                curr = curr.next

            curr.next = cur1 if cur1 else cur2
            return dummy.next

        if not lists:
            return None
        
        current = lists[0]

        l, r = 0, len(lists)
        def divide(arr):
            if not arr:
                return None
            if len(arr) == 1:
                return arr[0]
                
            mid =len(arr) // 2

            left = divide(arr[:mid])
            right = divide(arr[mid:])

            return mergeList(left,right)

        return divide(lists)

            



        








