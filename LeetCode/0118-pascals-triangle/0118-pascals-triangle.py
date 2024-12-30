class Solution(object):
    def generate(self, numRows):
        result = [[1]]
        # 맨 처음으로 1의 값 초기화했기에 numRows에서 1개를 뺀다.
        for i in range(numRows - 1):
            candidate = [1] # 맨 앞에는 1 고정
            # i는 이전의 인덱스이며 j는 인덱스의 1번부터 i길이만큼
            # 예를 들어 i가 1이면, j는 1,2까지, [1,2,1]을 만든다.
            # 그러면 이전의 [1,1]에서 이 둘을 인덱스 상 앞 뒤로 더하면서 다음 리스트에 추가해준다
            for j in range(1, i + 1):
                candidate.append(result[i][j] + result[i][j - 1])
            candidate.append(1) # 맨 뒤에는 1 고정
            result.append(candidate)
        return result