class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        list_freq = [0 for num in range(26)]
        wnd_left = 0
        max_freq = 0
        result = 0
        for idx in range(len(s)):
            max_freq = max(max_freq, list_freq[s[idx] - 'A'])
            while idx - wnd_left + 1 - max_freq > k:
                list_freq[s[wnd_left] - 'A'] -= 1
                wnd_left += 1
            result = max(result, idx - wnd_left + 1)
        return result

