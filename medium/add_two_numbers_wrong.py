from typing import List, Optional
from copy import copy
class ListNodeCustom:
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
    

class Solution:
    def array_to_list_node(self, array):
        cur_node = None
        for i in range(len(array)-1,-1,-1):
            declaring_node = ListNodeCustom(array[i])
            if i != len(array)-1:
                declaring_node.next = cur_node
            cur_node = declaring_node
        return cur_node
    
    def factory(self, ll):
        new_ll = None
        while ll.next:
            new_ll_aux = ListNodeCustom(ll.val)
            ll = ll.next
            new_ll = new_ll or new_ll_aux
            new_ll = new_ll_aux
        return new_ll
    
    def defactory(self, ll):
        new_ll = None
        while ll.next:
            new_ll_aux = ListNode(ll.val)
            ll = ll.next
            new_ll = new_ll or new_ll_aux
            new_ll = new_ll_aux
        return new_ll

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.factory(l1) or ListNodeCustom(0)
        l2 = self.factory(l2) or ListNodeCustom(0)
        assert l1.len() <= 100 and l1.len() > 0
        assert l2.len() <= 100 and l2.len() > 0
        num = l1.reverse().get_number()+l2.reverse().get_number()
        num = str(num)
        res = self.array_to_list_node([int(x) for x in num]).reverse()
        return self.defactory(res)
