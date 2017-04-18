import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        idx, square, nums = 1, 1, []
        while square <= n:
            if square == n:
                return 1
            nums.append(square)
            idx += 1
            square = idx * idx
        dict_dp = {}
        return self.help(nums, len(nums)-1, n, dict_dp)

    def help(self, nums, idx, target, dict_dp):
        print(idx, target)
        if idx == 0:
            return target
        if dict_dp.get((idx, target), None) is not None:
            return dict_dp[(idx, target)]
        result = sys.maxsize
        loop = int(target / nums[idx])
        for i in range(loop, -1, -1):
            target_this = target - nums[idx] * i
            if target_this == 0:
                result = i
                break
            result_this = i + self.help(nums, idx - 1, target_this, dict_dp)
            if result_this < result:
                result = result_this
            else:
                break
        dict_dp[(idx, target)] = result
        return result

my_solution = Solution()
print(my_solution.numSquares(12))

