# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        target = []
        node = head
        while node:
            target.append(node.val)
            node = node.next
        for i in range(len(target) // 2):
            if target[i] != target[-1-i]:
                return False
        return True
        