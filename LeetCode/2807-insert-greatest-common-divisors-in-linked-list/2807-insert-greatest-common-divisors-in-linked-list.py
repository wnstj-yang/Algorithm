# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        if head.next is None:
            return head
        
        # 유클리드 호제법
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        left = head
        while left.next:
            right = left.next
            big, small = left.val, right.val
            if left.val < right.val:
                big = right.val
                small = left.val
            gcd_val = gcd(big, small)
            node = ListNode(gcd_val)
            left.next = node
            node.next = right
            left = right
        return head
        