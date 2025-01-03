class Solution(object):
    def singleNumber(self, nums):
        """
        XOR를 활용한다.
        XOR는 교환법칙, 결합법칙을 적용한다.
        즉, 연산 순서를 바꾸거나 위치를 바꾸어도 결과가 같다.
        테스트케이스의 예를 들면, [4, 1, 2, 1, 2]로 하든, [2, 2, 1, 4, 1]로 하든 똑같다는 의미이다.
        (이진수로 바꾸어서 위치를 바꾸거나 연산해도 동일하듯이 보인다.)
        """
        answer = nums[0]
        for num in nums[1:]:
            answer ^= num
        return answer

        