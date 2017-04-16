from collections import deque


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        deque_result = self.help(candidates, target, 0)
        for idx in range(len(deque_result)):
            deque_result[idx] = list(deque_result[idx])
        # print(deque_result)
        return list(deque_result)

    def help(self, candidates, target, begin):
        deque_result = deque()
        for idx in range(begin, len(candidates)):
            if candidates[idx] > target:
                break
            if candidates[idx] == target:
                deque_now = deque()
                deque_now.append(candidates[idx])
                deque_result.append(deque_now)
            else:
                deque_this = self.help(candidates, target - candidates[idx], idx)
                for i in range(len(deque_this)):
                    deque_this[i].appendleft(candidates[idx])
                deque_result += deque_this
        return deque_result
