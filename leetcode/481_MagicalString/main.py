class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        sum_of_one = 1
        list_nums = [1, 2, 2]
        for idx in range(2, n):
            if list_nums[idx] == 1:
                sum_of_one += 1
            if len(list_nums) < n:
                num_add = 2
                if idx % 2 == 0:
                    num_add = 1
                for j in range(0, list_nums[idx]):
                    list_nums.append(num_add)
        return sum_of_one
