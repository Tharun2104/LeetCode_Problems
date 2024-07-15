"""
https://leetcode.com/problems/add-two-numbers/description/
"""
from typing import Optional
from ListNodeCreation import Linkedlist
from ListNodeCreation import ListNode


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        cur_point_1 = l1
        cur_point_2 = l2
        # print(cur_point_1)
        carry = 0
        while cur_point_1 or cur_point_2 or carry !=0:
            if(cur_point_1 is None and cur_point_2 is None):
                val1, val2 = 0, 0
            elif(cur_point_2 is None):
                val2 = 0
                val1 = cur_point_1.val
                cur_point_1 = cur_point_1.next
            elif(cur_point_1 is None):
                val1 = 0
                val2 = cur_point_2.val
                cur_point_2 = cur_point_2.next
            else:
                val1 = cur_point_1.val
                val2 = cur_point_2.val
                cur_point_1 = cur_point_1.next
                cur_point_2 = cur_point_2.next
            new_num = val1 + val2 + carry
            add_num = new_num%10
            carry = new_num//10
            new_node = ListNode(add_num)
            dummy.next = new_node
            dummy = dummy.next
        return temp.next
        

l1 = Linkedlist(9,9,9,9,9,9,9)
l2 = Linkedlist(9,9,9,9)
test = Solution().addTwoNumbers(l1.head,l2.head)
res = []  # for checking the result
while test:
    res.append(test.val)
    test = test.next
print(res)