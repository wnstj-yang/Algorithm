class Solution(object):
    def plusOne(self, digits):
        # 마지막 인덱스부터 0번까지 역으로 진행
        for i in range(len(digits) - 1, -1, -1):
            # 9인 경우 현재 값을 초기화하고 다음 인덱스에서 1을 추가해준다. 지속적으로 9인 경우 계속 0초기화
            if digits[i] == 9:
                digits[i] = 0
            # 9가 아닌 경우까지 왔으므로 현재 값을 더해주고 반환해준다. 추가적으로 0까지 갈 필요는 없다.
            else:
                digits[i] += 1
                return digits
        # 맨 왼쪽까지 온 경우이므로 1을 추가해서 반환해주어서 숫자를 맞춰준다
        return [1] + digits
