# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import List, Optional
from copy import copy
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        assert val >= 0 and val <= 9
        self.val = val
        self.next = next
    
    def reverse(self):
        node = copy(self)
        old_node = None
        while node:
            next_node = node.next
            node.next = old_node
            old_node = node
            node = next_node
        return old_node
    
    def get_number(self):
        node = self.reverse()
        i = 0
        number = 0
        while node:
            number+=node.val*10**i
            node=node.next
            i+=1
        return number
    
    def len(self):
        node = self
        i = 0
        while node:
            node=node.next
            i+=1
        return i
    
def array_to_list_node(array):
    cur_node = None
    for i in range(len(array)-1,-1,-1):
        declaring_node = ListNode(array[i])
        if i != len(array)-1:
            # cur_node = declaring_node
            declaring_node.next = cur_node
        cur_node = declaring_node
    return cur_node

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        assert l1.len() <= 100 and l1.len() > 0
        assert l2.len() <= 100 and l2.len() > 0
        num = l1.reverse().get_number()+l2.reverse().get_number()
        num = str(num)
        return array_to_list_node([int(x) for x in num]).reverse()

if __name__ == '__main__':
    l = array_to_list_node([1,2,3,4])
    print(l.reverse().get_number())
    s = Solution()
    ll = array_to_list_node # linked list
    print(f"{s.addTwoNumbers(ll([2,4,3]), ll([5,6,4])).get_number()=}")
    print(f"{s.addTwoNumbers(ll([0]), ll([0])).get_number()=}")
    print(f"{s.addTwoNumbers(ll([9,9,9,9,9,9,9]), ll([9,9,9,9])).get_number()=}")
    