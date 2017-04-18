import copy

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        len_primes = len(primes)
        list_cur = copy.copy(primes)
        list_idx = [0 for idx in range(len_primes)]
        list_result = [1]
        while len(list_result) < n:
            num_min = min(list_cur)
            list_result.append(num_min)
            for idx in range(len_primes):
                if list_cur[idx] == num_min:
                    list_idx[idx] += 1
                    list_cur[idx] = primes[idx] * list_result[list_idx[idx]]
        return list_result[len(list_result)-1]
