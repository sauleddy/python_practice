import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_nums = {}
        self.list_nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        idx = self.dict_nums.get(val, None)
        if idx is None:
            self.list_nums.append(val)
            self.dict_nums[val] = len(self.list_nums) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        idx = self.dict_nums.get(val, None)
        if idx is None:
            return False
        else:
            len_nums = len(self.list_nums)
            if len_nums > 1:
                self.dict_nums[self.list_nums[-1]] = idx
                self.list_nums[idx] = self.list_nums[-1]
            del self.list_nums[-1]
            del self.dict_nums[val]
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.list_nums[random.randint(0, len(self.list_nums) - 1)]

        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()
