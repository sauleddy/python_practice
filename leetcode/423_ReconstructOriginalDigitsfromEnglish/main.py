from collections import Counter


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_order = [8, 0, 3, 2, 6, 7, 4, 5, 9, 1]
        list_letter = ['z', 'o', 'w', 'h', 'r', 'f', 'x', 's', 'g', 'i']
        list_counter = [Counter('zero'),
                        Counter('one'),
                        Counter('two'),
                        Counter('three'),
                        Counter('four'),
                        Counter('five'),
                        Counter('six'),
                        Counter('seven'),
                        Counter('eight'),
                        Counter('nine')]
        counter_freq = Counter(s)
        str_result = ''
        for idx in range(len(list_order)):
            number = list_order[idx]
            while counter_freq.get(list_letter[number], 0) > 0:
                str_result += str(number)
                counter_freq -= list_counter[number]
        str_result = ''.join(sorted(str_result))
        return str_result


mySolution = Solution()
print(mySolution.originalDigits('owoztneoer'))
