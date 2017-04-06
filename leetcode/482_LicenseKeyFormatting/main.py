class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        str_res = ''
        S = S.replace('-', '')
        S = S.upper()
        while len(S) > K:
            str_res = '-' + S[-K:] + str_res
            S = S[:-K]
        if len(S) > 0:
            str_res = S + str_res
        else:
            str_res = str_res[1:]

        return str_res

mySolution = Solution()
print(mySolution.licenseKeyFormatting('2-4A0r7-4k', 3))
