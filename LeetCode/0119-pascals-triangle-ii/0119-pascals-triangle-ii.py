class Solution(object):
    def getRow(self, rowIndex):
        result = [[1]]
        for i in range(rowIndex):
            candidate = [1]
            for j in range(1, i + 1):
                candidate.append(result[i][j] + result[i][j - 1])
            candidate.append(1)
            result.append(candidate)
        return result[rowIndex]
        