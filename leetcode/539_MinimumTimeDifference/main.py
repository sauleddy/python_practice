class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        list_minutes = []
        for idx in range(len(timePoints)):
            list_h_m = timePoints[idx].split(":")
            hour_this = int(list_h_m[0])
            min_this = int(list_h_m[1])
            list_minutes.append(hour_this * 60 + min_this)

        diff_min = None
        mins_per_day = 24 * 60
        list_minutes = sorted(list_minutes)
        for idx in range(0, len(list_minutes)):
            time_min = list_minutes[idx - 1]
            time_max = list_minutes[idx]
            if idx == 0:
                time_min, time_max = time_max, time_min
            diff1 = time_max - time_min
            diff_min_this = min(diff1, mins_per_day - diff1)
            if diff_min is None or diff_min > diff_min_this:
                diff_min = diff_min_this
        return diff_min

