# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1_str, l2_str = '', ''
        while l1:
            l1_str = str(l1.val) + l1_str
            l1 = l1.next
        while l2:
            l2_str = str(l2.val) + l2_str
            l2 = l2.next
        two_sum = list(str(int(l1_str) + int(l2_str)))
        two_sum.reverse()
        result = ListNode()
        res = result
        for n in two_sum:
            n = int(n)
            node = ListNode(n)
            result.next = node
            result = result.next
        return res.next