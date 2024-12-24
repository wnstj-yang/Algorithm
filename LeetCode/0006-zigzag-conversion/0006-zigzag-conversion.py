class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        result = ''
        rows = [[] for _ in range(numRows)]
        index = 0
        flag = True # 행 위아래 방향을 나타내주는 flag 값, True면 행 증가, False면 행 감소
        for alphabet in s:
            rows[index].append(alphabet)
            if index == 0:
                flag = True
            elif index == numRows - 1:
                flag = False
            if flag:
                index += 1
            else:
                index -= 1
        for row in rows:
            result += ''.join(row)
        return result


        