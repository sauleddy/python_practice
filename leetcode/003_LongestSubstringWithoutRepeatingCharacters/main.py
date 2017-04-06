class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        if len_s <= 1:
            return len_s
        wnd_left = 0
        dict_freq = {s[0]: 0}
        result = 0
        for idx in range(len_s):
            if dict_freq.get(s[idx], -1) == -1 or dict_freq[s[idx]] < wnd_left:
                result = max(result, idx - wnd_left + 1)
            else:
                wnd_left = dict_freq[s[idx]] + 1

            dict_freq[s[idx]] = idx
