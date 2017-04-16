from heapq import *

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heapify(nums)
        return nlargest(k, nums)[k-1]

