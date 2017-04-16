class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        list_sorted = sorted(candidates)
        list_result = self.help(list_sorted, 0, target)
        set_result = set()
        for item in list_result:
            set_result.add(tuple(item))
        list_final = []
        for item in list(set_result):
            item = list(reversed(item))
            list_final.append(list(item))
        return list_final

    def help(self, candidates, idx, target):
        len_candidates = len(candidates)
        if idx >= len_candidates or candidates[idx] > target:
            return []
        if candidates[idx] == target:
            return [[candidates[idx]]]
        list_contain = self.help(candidates, idx+1, target-candidates[idx])
        list(map(lambda x: x.append(candidates[idx]), list_contain))
        list_not_contain = self.help(candidates, idx+1, target)
        list_sum = list_contain + list_not_contain
        return list_sum

# list_test = [[1, 2], [3]]
# list(map(lambda x: x.append(4), list_test))
# print(list_test)

my_solution = Solution()
print(my_solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
