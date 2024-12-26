class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        container = 0
        while left < right:
            calculate = (right - left) * min(height[left], height[right])
            container = max(container, calculate)
            # 오른쪽의 높이가 왼쪽 높이보다 크면 왼쪽을 늘리고, 반대는 오른쪽을 줄인다.(인덱스)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return container

        