# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head == []:
            return head
        
        # 맨 앞의 None, 즉 prev의 값을 연결해준다.
        # 결과적으로 연결 방향을 역으로 바꿔줘야한다.
        prev = None
        now = head
        while now:
            next_node = now.next # 다음 노드
            now.next = prev # 현재 노드의 next가 앞을 바라보도록 변경
            prev = now # 이전 노드는 현재 노드로
            now = next_node # 현재 노드는 다음 노드로 변경
        return prev
        