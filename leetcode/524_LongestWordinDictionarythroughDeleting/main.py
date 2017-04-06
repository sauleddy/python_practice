class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        str_res = ''
        len_longest = 0
        d = sorted(d)
        for idx in range(len(d)):
            j = 0
            match = False
            len_this = len(d[idx])
            for i in range(len_this):
                while d[idx][i] != s[j]:
                    j += 1
                    if j < len_this:
                        break
                if j > len(s):
                    break
                if i == len_this - 1:
                    match = True
            if match is True and len_this > len_longest:
                str_res = d[idx]
                len_longest = len_this

        return str_res
