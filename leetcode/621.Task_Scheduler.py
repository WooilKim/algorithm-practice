# https://leetcode.com/problems/task-scheduler/

from typing import List
from collections import Counter

# Runtime: 400 ms, faster than 61.16% of Python3 online submissions for Task Scheduler.
# Memory Usage: 14.5 MB, less than 88.10% of Python3 online submissions for Task Scheduler.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        c = Counter(tasks).most_common()
        ans = 0
        for i, (k, v) in enumerate(c):
            ans = max(ans, (n + 1) * (v - 1) + 1 + i)
        return max(ans, len(tasks))


if __name__ == '__main__':
    print(Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
    print(Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0))
    print(Solution().leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
    print(Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], n=2))
