# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        if list1: 
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next


   


        # cur1 = list1
        # cur2 = list2
        # head = ListNode(0)
        # curr = head
        
        # while cur1 and cur2:
            
        #     if cur1.val <= cur2.val: 
        #         curr.next = cur1
        #         cur1 = cur1.next
            
        #     else:
        #         curr.next = cur2
        #         cur2 = cur2.next
            
        #     curr = curr.next
        # curr.next = cur1 if cur1 else cur2
        # return head.next


        






























