# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        result = []
        cnt = 0
        node = head.next
        while node:
            cnt += node.val
            if node.val == 0:
                result.append(cnt)
                cnt = 0
            node = node.next
        answer = ListNode(result[0])
        head = answer
        for num in result[1:]:
            head.next = ListNode(num)
            head = head.next
        return answer
            
        