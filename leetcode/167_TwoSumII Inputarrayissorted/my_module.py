class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        dict_value_idx = {}
        list_return = []
        for i in range(len(numbers)):
            num = target - numbers[i]
            if num in dict_value_idx:
                list_return.append(dict_value_idx[num] + 1)
                list_return.append(i + 1)
                break
            else:
                dict_value_idx[numbers[i]] = i

        return list_return
        """
        list_return = []
        idx_left = 0
        idx_right = len(numbers) - 1
        while idx_left < idx_right:
            sum_of_two = numbers[idx_left] + numbers[idx_right]
            if sum_of_two == target:
                list_return.append(idx_left + 1)
                list_return.append(idx_right + 1)
                break
            elif sum_of_two > target:
                idx_right -= 1
            else:
                idx_left += 1
        return list_return
