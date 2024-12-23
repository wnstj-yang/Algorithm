# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        N = 0 # 연결리스트의 총 길이
        result = []
        node = head
        # 1. 연결리스트의 총 길이를 알아보자 
        while node:
            N += 1
            node = node.next
        # 2. 연결리스트의 총 길이 중 절반까지의 연결리스트의 head를 넘긴다
        for _ in range(N // 2):
            head = head.next
        return head
        