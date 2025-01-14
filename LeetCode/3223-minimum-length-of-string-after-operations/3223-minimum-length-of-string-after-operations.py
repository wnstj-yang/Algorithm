class Solution(object):
    def minimumLength(self, s):
        alpha_list = [0] * 26
        # s 문자열에 대해서 각 개수만큼 더해주기
        for string in s:
            alpha_list[ord(string) - ord('a')] += 1
        # 순회하면서 2개 초과하는 경우에는 왼쪽, 오른쪽 하나씩 감소한다고 판단하여 2씩 빼준다
        for string in s:
            index = ord(string) - ord('a')
            if alpha_list[index] > 2:
                alpha_list[index] -= 2
        # 조건을 거친 이후 합을 반환한다.
        return sum(alpha_list)
        