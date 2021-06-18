# https://leetcode.com/problems/meeting-rooms-ii/
# 253. Meeting Rooms II

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        e = ret = 0
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)

        for s in range(len(start)):
            if start[s] < end[e]:
                ret += 1
            else:
                e += 1
        return ret


if __name__ == '__main__':
    print(Solution().minMeetingRooms(intervals=[[0, 30], [5, 10], [15, 20]]))
