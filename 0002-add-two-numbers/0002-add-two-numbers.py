# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        dummy = ListNode()
        res_node = dummy
        carry = 0
        while cur1 or cur2 or carry:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            res = val1 + val2 + carry
            if(res>=10):
                res, carry = res-10, 1
            else:
                carry = 0

            # updating the pointers
            dummy.next = ListNode(res)
            dummy = dummy.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

        return res_node.next
        
        # while(cur1):
        #     res = cur1.val + carry
        #     if(res>=10):
        #         res, carry = res-10, 1
        #     else:
        #         carry = 0   
        #     # updating the pointers
        #     dummy.next = ListNode(res)
        #     dummy = dummy.next
        #     cur1 = cur1.next
        
        # while(cur2):
        #     res = cur2.val + carry
        #     if(res>=10):
        #         res, carry = res-10, 1
        #     else:
        #         carry = 0   
        #     # updating the pointers
        #     dummy.next = ListNode(res)
        #     dummy = dummy.next
        #     cur2 = cur2.next
        
        # if(carry):
        #     dummy.next = ListNode(carry)

        # return res_node.next
            