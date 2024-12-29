class Solution(object):
    # candidates만큼 길이의 조합을 구하면 시간 초과 발생
    # target을 기준으로 백트래킹 진행
    # 매개변수의 target이 0이면 배열의 합이 맞으므로 정답 리스트 중 하나
    # target이 1 이상이므로 0보다 작으면 백트래킹 진행
    # 이외 순서대로 candidates 내의 값을 인덱스 따라 진행
    def combinationSum(self, candidates, target):
        def backtrack(idx, target, path):
            # target
            if target < 0:
                return

            if target == 0:
                result.append(path)
                return
            for i in range(idx, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])
        result = []
        backtrack(0, target, [])
        return result
        

        