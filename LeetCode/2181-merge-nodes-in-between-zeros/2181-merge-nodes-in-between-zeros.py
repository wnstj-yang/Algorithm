# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        part = head # 합산된 값들을 새로운 값으로 초기화하는 파트
        search = head.next # 0을 만날때까지 val을 더하면서 찾아나서는 파트
        while search:
            cnt = 0
            while search.val != 0:
                cnt += search.val
                search = search.next
            search = search.next # 0이되어 빠져나왔으므로 그 다음 노드로 이동
            # 초기는 0값을 가지므로, 다음 노드로 이동 후 합산된 값으로 초기화
            part = part.next
            part.val = cnt
        part.next = None # 이후 값들을 None으로 초기화해준다.
        return head.next
            


# 방법 1
# class Solution(object):
#     def mergeNodes(self, head):
#         result = []
#         cnt = 0
#         node = head.next
#         while node:
#             cnt += node.val
#             if node.val == 0:
#                 result.append(cnt)
#                 cnt = 0
#             node = node.next
#         answer = ListNode(result[0])
#         head = answer
#         for num in result[1:]:
#             head.next = ListNode(num)
#             head = head.next
#         return answer