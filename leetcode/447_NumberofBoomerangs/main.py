class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        num_boomerangs = 0
        num_point = len(points)
        for pivot in range(num_point):
            dict_distance = {}
            for idx in range(num_point):
                distance = (points[pivot][0] - points[idx][0]) ** 2 + \
                           (points[pivot][1] - points[idx][1]) ** 2
                dict_distance[distance] = dict_distance.get(distance, 0) + 1
            for value in dict_distance.values():
                if value > 1:
                    num_boomerangs += value * (value - 1)

        return num_boomerangs
