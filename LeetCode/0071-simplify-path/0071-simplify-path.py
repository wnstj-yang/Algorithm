class Solution(object):
    def simplifyPath(self, path):
        split_path = path.split('/') # '/'를 기준으로 하나씩 나눈다. 
        stack = []
        for p in split_path:
            # 빈 값이거나 현재 위치를 나타내면 건너뛴다.
            if p == '' or p == '.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        # 각 리스트에 있는 것을 join 메서드로 구분자와 함께 합쳐준다
        return '/' + '/'.join(stack)